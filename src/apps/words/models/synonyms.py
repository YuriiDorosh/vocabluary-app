from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class WordSynonym(TimedAndUnixIdBaseModel):
    main_word = models.ForeignKey(
        verbose_name=_("Main word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="synonyms",
    )
    synonym_word = models.ForeignKey(
        verbose_name=_("Synonym word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="similar_words",
    )
    
    class Meta:
        db_table = "words_word_synonym"
        verbose_name = _("Word Synonym")
        verbose_name_plural = _("Word Synonyms")
        
    def __str__(self) -> str:
        return f"Main: {self.main_word} | Synonym: {self.synonym_word}"
