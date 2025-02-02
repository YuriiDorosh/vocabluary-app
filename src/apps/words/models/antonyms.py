from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class WordAntonym(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="antonyms",
    )
    text = models.TextField(
        verbose_name=_("Antonym text"),
        null=False,
        blank=False,
    )

    class Meta:
        db_table = "words_word_antonym"
        verbose_name = _("Word Antonym")
        verbose_name_plural = _("Word Antonymys")
        
    def __str__(self) -> str:
        return f"{self.word} - {self.text}"