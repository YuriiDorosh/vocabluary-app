from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class UserCategory(TimedAndUnixIdBaseModel):
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="categories",
    )
    category = models.CharField(
        verbose_name=_("Category"),
        max_length=255,
        null=False,
        blank=False,
    )
    is_public = models.BooleanField(
        verbose_name=_("Is public"),
        null=False,
        blank=False,
    )
    
    class Meta:
        db_table = "words_user_category"
        verbose_name = _("User Category")
        verbose_name_plural = _("User Categories")
        
    def __str__(self) -> str:
        return f"{self.user} - {self.category}"
    
    
class WordCategory(TimedAndUnixIdBaseModel):
    user_category = models.ForeignKey(
        verbose_name=_("User category"),
        to=UserCategory,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="word_categories",
    )
    word = models.ForeignKey(
        verbose_name=_("Word"),
        to="words.Word",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="categories",
    )
    
    class Meta:
        db_table = "words_word_category"
        verbose_name = _("Word Category")
        verbose_name_plural = _("Word Categories")
        
    def __str__(self) -> str:
        return f"{self.user_category} - {self.word}"