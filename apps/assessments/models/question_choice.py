# Django Imports
from django.db import models

# HTK Imports
from htk.apps.assessments.models.fk_fields import fk_question
from htk.models.classes import HtkBaseModel


DEFAULT_RELATED_NAME = 'choices'


class QuestionChoice(HtkBaseModel):
    question = fk_question(DEFAULT_RELATED_NAME, required=True)
    text = models.TextField(max_length=256)
    order = models.PositiveSmallIntegerField(default=0)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Assessment Question Choice'
