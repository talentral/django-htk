# Django Imports
from django.db import models

# HTK Imports
from htk.apps.assessments.models.fk_fields import (
    fk_assessment,
    fk_question,
)
from htk.models.classes import HtkBaseModel


DEFAULT_RELATED_NAME = 'answer_key'
DEFAULT_RELATED_NAME_PLURAL = 'answer_keys'


class AssessmentQuestionAnswerKey(HtkBaseModel):
    assessment = fk_assessment(DEFAULT_RELATED_NAME_PLURAL, required=True)
    question = fk_question(DEFAULT_RELATED_NAME, required=True, one_to_one=True)

    class Meta:
        verbose_name = 'Assessment Question Answer Key'
