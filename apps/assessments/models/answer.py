# Django Imports
from django.db import models

# HTK Imports
from htk.apps.assessments.models.fk_fields import (
    fk_question,
    fk_question_choice,
)
from htk.models.classes import HtkBaseModel
from htk.models.fk_fields import fk_user


DEFAULT_RELATED_NAME = 'answers'


class Answer(HtkBaseModel):
    user = fk_user(DEFAULT_RELATED_NAME, required=True)
    question = fk_question(DEFAULT_RELATED_NAME, required=True)
    choice = fk_question_choice(DEFAULT_RELATED_NAME)

    class Meta:
        verbose_name = 'Assessment Question Answer'
