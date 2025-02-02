from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class WordEtymology(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="etymologies",
    )
    text = models.TextField(
        verbose_name=_("Etymology text"),
        null=False,
        blank=False,
    )

    class Meta:
        db_table = "words_word_etymology"
        verbose_name = _("Word Etymology")
        verbose_name_plural = _("Word Etymologies")
        
    def __str__(self) -> str:
        return f"{self.word} - {self.text}"