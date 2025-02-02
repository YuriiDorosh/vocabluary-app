from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class WordExample(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="examples",
    )
    text = models.TextField(
        verbose_name=_("Example text"),
        null=False,
        blank=False,
    )

    class Meta:
        db_table = "words_word_example"
        verbose_name = _("Word Example")
        verbose_name_plural = _("Word Examples")
        
    def __str__(self) -> str:
        return f"{self.word} - {self.text}"
