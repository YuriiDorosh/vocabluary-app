import json
from channels.db import database_sync_to_async
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin, action
from djangochannelsrestframework.observer import model_observer

from django.contrib.auth.models import User
from src.apps.chats.models import Room as RoomModel, RoomUser as RoomUserModel, Message as MessageModel
from src.api.v1.dcrf.chats.serializers.message_serializer import MessageSerializer
from src.api.v1.dcrf.chats.serializers.room_serializer import RoomSerializer
from src.api.v1.drf.users.serializers.user_serializer import UserSerializer

class RoomConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "pk"

    async def disconnect(self, code):
        if hasattr(self, "room_subscribe"):
            await self.remove_user_from_room(self.room_subscribe)
            await self.notify_users()
        await super().disconnect(code)

    @action()
    async def join_room(self, pk, **kwargs):
        self.room_subscribe = pk
        await self.add_user_to_room(pk)
        await self.notify_users()

    @action()
    async def leave_room(self, pk, **kwargs):
        await self.remove_user_from_room(pk)
        await self.notify_users()

    @action()
    async def create_message(self, message, **kwargs):
        room = await self.get_room(pk=self.room_subscribe)
        user = self.scope["user"]
        await database_sync_to_async(MessageModel.objects.create)(
            room=room, user=user, text=message
        )

    @model_observer(MessageModel)
    async def message_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @message_activity.groups_for_signal
    def message_activity_groups_for_signal(self, instance: MessageModel, **kwargs):
        yield f"room__{instance.room_id}"

    @message_activity.groups_for_consumer
    def message_activity_groups_for_consumer(self, room=None, **kwargs):
        if room is not None:
            yield f"room__{room}"

    @message_activity.serializer
    def message_activity_serializer(self, instance: MessageModel, action, **kwargs):
        return {
            "data": MessageSerializer(instance).data,
            "action": action.value,
            "pk": instance.pk,
        }

    async def notify_users(self):
        room = await self.get_room(pk=self.room_subscribe)
        for group in self.groups:
            await self.channel_layer.group_send(
                group,
                {
                    "type": "update_users",
                    "usuarios": await self.current_users(room),
                },
            )

    async def update_users(self, event):
        await self.send(json.dumps({"usuarios": event["usuarios"]}))

    @database_sync_to_async
    def get_room(self, pk):
        return RoomModel.objects.get(pk=pk)

    @database_sync_to_async
    def current_users(self, room):
        room_users = RoomUserModel.objects.filter(room=room)
        users = [ru.user for ru in room_users]
        return UserSerializer(users, many=True).data

    @database_sync_to_async
    def remove_user_from_room(self, pk):
        user = self.scope["user"]
        room = RoomModel.objects.get(pk=pk)
        RoomUserModel.objects.filter(room=room, user=user).delete()

    @database_sync_to_async
    def add_user_to_room(self, pk):
        user = self.scope["user"]
        room = RoomModel.objects.get(pk=pk)
        if not RoomUserModel.objects.filter(room=room, user=user).exists():
            RoomUserModel.objects.create(room=room, user=user)

class UserConsumer(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DeleteModelMixin,
    GenericAsyncAPIConsumer,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer