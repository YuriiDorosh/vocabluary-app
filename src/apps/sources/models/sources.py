from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel
from src.apps.words.models import Word


class Source(TimedAndUnixIdBaseModel):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=256,
        null=False,
        blank=False,
    )
    url = models.URLField(
        verbose_name=_("Source URL"),
        max_length=512,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        verbose_name=_("Created by this user"),
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,        
        related_name="sources",
    )
    
    class Meta:
        db_table = "sources_source"
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")
        
    def __str__(self) -> str:
        return f"Word: {self.name}"
    
    
class WordSource(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to=Word,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="sources",
    )
    source = models.ForeignKey(
        verbose_name="Source",
        to=Source,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="words",
    )
    part_of_speech_text = models.TextField(
        verbose_name=_("Part of Speech"),
        null=True,
        blank=True,
    )
    
    class Meta:
        db_table = "sources_source_word"
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")
        
    def __str__(self) -> str:
        return f"Word: {self.name}"