from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel
from src.apps.words.enums.levels import LevelEnum


class Word(TimedAndUnixIdBaseModel):
    word = models.CharField(
        verbose_name=_("Word"),
        max_length=256,
        null=False,
        blank=False,
    )
    definition = models.TextField(
        verbose_name=_("Definition"),
        null=True,
        blank=True,
    )
    level = models.CharField(
        verbose_name=_("Word Level"),
        max_length=2,
        choices=LevelEnum.choices,
        default=LevelEnum.Intermediate,
    )
    owner = models.ForeignKey(
        verbose_name=_("Created by this user"),
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,        
        related_name="words",
    )
    
    class Meta:
        db_table = "words_words"
        verbose_name = _("Word")
        verbose_name_plural = _("Words")
        
    def __str__(self) -> str:
        return f"Word: {self.word}"
