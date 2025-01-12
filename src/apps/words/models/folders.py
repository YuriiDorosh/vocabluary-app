from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class Folder(TimedAndUnixIdBaseModel):
    name = models.CharField(
        verbose_name=_("Folder name"),
        max_length=512,
        null=False,
        blank=False,
    )
    parent_folder = models.ForeignKey(
        verbose_name="Parent folder",
        to="self",
        on_delete=models.CASCADE,
        
    )