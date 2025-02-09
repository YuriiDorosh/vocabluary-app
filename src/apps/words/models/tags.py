from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class UserTag(TimedAndUnixIdBaseModel):
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="tags",
    )
    tag = models.CharField(
        verbose_name=_("Tag"),
        max_length=255,
        null=False,
        blank=False,
    )
    
    class Meta:
        db_table = "words_user_tag"
        verbose_name = _("User Tag")
        verbose_name_plural = _("User Tags")
        
    def __str__(self) -> str:
        return f"{self.user} - {self.tag}"
    
    
class WordTag(TimedAndUnixIdBaseModel):
    user_tag = models.ForeignKey(
        verbose_name=_("User tag"),
        to=UserTag,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="word_tags",
    )
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="tags",
    )
    
    class Meta:
        db_table = "words_word_tag"
        verbose_name = _("Word Tag")
        verbose_name_plural = _("Word Tags")
        
    def __str__(self) -> str:
        return f"{self.user_tag} - {self.word}"
