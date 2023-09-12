# Django Imports
from django.db import models

# HTK Imports
from htk.models.fk_fields import build_kwargs
from htk.utils import htk_setting


def fk_assessment(related_name, required=False):
    field = models.ForeignKey(
        htk_setting('HTK_ASSESSMENTS_ASSESSMENT_MODEL'),
        related_name=related_name,
        **build_kwargs(required=required),
    )
    return field


def fk_question(related_name, required=False):
    field = models.ForeignKey(
        htk_setting('HTK_ASSESSMENTS_QUESTION_MODEL'),
        related_name=related_name,
        **build_kwargs(required=required),
    )
    return field


def fk_question_choice(related_name, required=False):
    field = models.ForeignKey(
        htk_setting('HTK_ASSESSMENTS_QUESTION_MODEL'),
        related_name=related_name,
        **build_kwargs(required=required),
    )
    return field
