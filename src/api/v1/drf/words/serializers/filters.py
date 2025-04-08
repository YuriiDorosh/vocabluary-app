from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from src.apps.words.enums.levels import LevelEnum


class WordFilterSerializer(serializers.Serializer):
    word = serializers.CharField(required=False, help_text=_("Filter by word (word__icontains)"))
    definition = serializers.CharField(required=False, help_text=_("Filter by definition (definition__icontains)"))
    level = serializers.ChoiceField(
        required=False,
        choices=LevelEnum.choices,
        help_text=_("Filter by level"),
    )