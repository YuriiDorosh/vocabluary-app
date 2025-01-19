from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class Room(TimedAndUnixIdBaseModel):
    name = models.CharField(
        verbose_name=_("Room name"),
        max_length=255, 
        null=False, 
        blank=False, 
        unique=True
    )
    host = models.ForeignKey(
        verbose_name=_("Created by this user"),
        to=User, 
        on_delete=models.CASCADE, 
        related_name="rooms",
    )

    class Meta:
        db_table = "chats_rooms"
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")

    def __str__(self):
        return f"Room({self.name} {self.host.username})"
    
    
class RoomUser(TimedAndUnixIdBaseModel):
    room = models.ForeignKey(
        verbose_name=_("Room User"),
        to=Room,
        on_delete=models.CASCADE,
        related_name="users",
    )
    user = models.ForeignKey(
        verbose_name=_("User Room"),
        to=User,
        on_delete=models.CASCADE,
        related_name="current_rooms",
    )
    
    class Meta:
        db_table = "chats_room_user"
        verbose_name = _("Room User")
        verbose_name_plural = _("Room Users")

    def __str__(self):
        return f"Room: {self.room.name} User: {self.user.username}"
