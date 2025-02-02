from django.db import models
from django.utils.translation import gettext_lazy as _

class LevelEnum(models.TextChoices):
    Begginer = 'A1', _('Begginer')
    Elementary = 'A2', _('Elementary')
    Intermediate = 'B1', _('Intermediate')
    UpperIntermediate = 'B2', _('Upper Intermediate')
    Advanced = 'C1', _('Advanced')
    Proficiency = 'C2', _('Proficiency')
