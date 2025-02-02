from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel
from src.apps.words.models import Word


class Note(TimedAndUnixIdBaseModel):
    text = models.TextField(
        verbose_name=_("Note text"),
        null=False,
        blank=False,
    )
    
    class Meta:
        db_table = "notes_note"
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
        
    def __str__(self) -> str:
        return f"{self.text}"
    
    
class WordNote(TimedAndUnixIdBaseModel):
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to=Word,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="notes",
    )
    note = models.ForeignKey(
        verbose_name=_("Note"),
        to=Note,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="words",
    )
    
    class Meta:
        db_table = "notes_note_words"
        verbose_name = _("Note Word")
        verbose_name_plural = _("Note Words")
        
    def __str__(self) -> str:
        return f"{self.word} - {self.note}"
