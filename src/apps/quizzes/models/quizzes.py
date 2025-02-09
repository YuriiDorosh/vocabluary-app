from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class Quiz(TimedAndUnixIdBaseModel):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("Is active"),
        null=False,
        blank=False,
    )
    is_public = models.BooleanField(
        verbose_name=_("Is public"),
        default=False,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="quizzes",
    )
    
    class Meta:
        db_table = "quizzes_quiz"
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        
    def __str__(self) -> str:
        return f"{self.title} - {self.description} - {self.is_active} - {self.is_public} - {self.user}"