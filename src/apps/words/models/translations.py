from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel
from src.apps.words.enums.languages import LanguageEnum


class WordTranslation(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name=_("Word translation"),
        to="apps.words.models.Word",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    translation_text = models.TextField(
        verbose_name=_("Translation text"),
        null=True,
        blank=True,
    )
    language = models.CharField(
        verbose_name=_("Language"),
        max_length=5,
        choices=LanguageEnum.choices,
        default=LanguageEnum.ENGLISH,
    )
    
    class Meta:
        db_table = "words_word_translations"
        verbose_name = _("Word translation")
        verbose_name_plural = _("Words translations")
        
        def __str__(self) -> str:
            return f"Word: {self.word.word} with translation {self.translation_text} | Language: {self.language}"
