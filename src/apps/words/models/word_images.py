from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class WordImage(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="images",
    )
    image = models.ImageField(
        verbose_name=_("Word image"),
        upload_to="uploads/% Y/% m/% d/",
        null=False,
        blank=False,
    )
    
    class Meta:
        db_table = "words_word_image"
        verbose_name = _("Word Image")
        verbose_name_plural = _("Word Images")
        
    def __str__(self) -> str:
        return f"{self.word}"