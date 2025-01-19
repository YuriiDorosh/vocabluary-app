from rest_framework import serializers
from src.apps.chats.models import Message as MessageModel
from src.api.v1.drf.users.serializers.user_serializer import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    created_at_formatted = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = MessageModel
        fields = "__all__"
        depth = 1

    def get_created_at_formatted(self, obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M:%S")