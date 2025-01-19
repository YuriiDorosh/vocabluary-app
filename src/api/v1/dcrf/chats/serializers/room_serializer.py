from rest_framework import serializers
from src.apps.chats.models import Room as RoomModel, RoomUser as RoomUserModel
from src.api.v1.dcrf.chats.serializers.message_serializer import MessageSerializer
from src.api.v1.drf.users.serializers.user_serializer import UserSerializer


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    current_users = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = RoomModel
        fields = ["id", "name", "host", "messages", "current_users", "last_message"]

    def get_last_message(self, obj):
        last_msg = obj.messages.order_by("-created_at").first()
        return MessageSerializer(last_msg).data if last_msg else None

    def get_current_users(self, obj):
        room_users = RoomUserModel.objects.filter(room=obj)
        users = [ru.user for ru in room_users]
        return UserSerializer(users, many=True).data
