from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.common.models import TimedAndUnixIdBaseModel


class QuizzQuestion(TimedAndUnixIdBaseModel):
    question = models.TextField(
        verbose_name=_("Question"),
        null=False,
        blank=False,
    )
    is_correct = models.BooleanField(
        verbose_name=_("Is correct"),
        null=False,
        blank=False,
    )
    question_order = models.PositiveIntegerField(
        verbose_name=_("Question order"),
        null=False,
        blank=False,
    )
    quiz = models.ForeignKey(
        verbose_name=_("Quiz"),
        to="quizzes.Quiz",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="questions",
    )
    
    class Meta:
        db_table = "quizzes_quizz_question"
        verbose_name = _("Quizz Question")
        verbose_name_plural = _("Quizz Questions")
        
    def __str__(self) -> str:
        return f"{self.question} - {self.is_correct} - {self.question_order} - {self.quiz}"
