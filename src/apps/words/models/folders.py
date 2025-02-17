from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel
from src.apps.words.models.words import Word


class Folder(TimedAndUnixIdBaseModel):
    name = models.CharField(
        verbose_name=_("Folder name"),
        max_length=256,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        verbose_name=_("Folder created by this user"),
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,        
        related_name="folders",
    )
    parent_folder = models.ForeignKey(
        verbose_name="Parent folder",
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children_folders",
    )
    
    class Meta:
        db_table = "words_folder"
        verbose_name = _("Folder")
        verbose_name_plural = _("Folders")
        
    def __str__(self) -> str:
        return f"Folder with id: {self.id} and name {self.name}"
    

class WordFolder(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name="Word",
        to=Word,
        null=True,
        blank=True,
        related_name="foplders",
        on_delete=models.CASCADE,
    )
    folder = models.ForeignKey(
        verbose_name="Folder",
        to=Folder,
        null=True,
        blank=True,
        related_name="words",
        on_delete=models.CASCADE,
    )
    
    class Meta:
        db_table = "words_word_folder"
        verbose_name = _("Folder word")
        verbose_name_plural = _("Folder words")
        
    def __str__(self) -> str:
        return f"TEMP" # TODO
