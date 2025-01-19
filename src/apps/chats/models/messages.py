from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class Message(TimedAndUnixIdBaseModel):
    room = models.ForeignKey(
        verbose_name=_("Room"),
        to="chats.Room", 
        on_delete=models.CASCADE, 
        related_name="messages",
    )
    text = models.TextField(
        verbose_name=_("Message text"),
        max_length=500,
    )
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User, 
        on_delete=models.CASCADE, 
        related_name="messages"
    )
    
    class Meta:
        db_table = "chats_message"
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return f"Message({self.user.username} {self.room.name})"