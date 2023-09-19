# Python Standard Library Imports
import random

# Django Imports
from django.db import models

# HTK Imports
from htk.apps.assessments.choices import get_question_type_choices
from htk.apps.assessments.enums import QuestionType
from htk.apps.assessments.models.fk_fields import fk_assessment
from htk.models.classes import HtkBaseModel


DEFAULT_RELATED_NAME = 'questions'


class AssessmentQuestion(HtkBaseModel):
    assessment = fk_assessment(DEFAULT_RELATED_NAME, required=True)
    type = models.PositiveIntegerField(
        choices=get_question_type_choices(), default=QuestionType.UNSPECIFIED
    )
    text = models.TextField(max_length=512)
    order = models.PositiveSmallIntegerField(default=0)
    should_shuffle_choices = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Assessment Question'

    ##
    # Properties

    @property
    def choices_ordered(self):
        choices = self.choices.order_by('order')
        return choices

    @property
    def choices_shuffled(self):
        choices = self.choices.all()
        random.shuffle(choices)
        return choices

    @property
    def all_choices(self):
        choices = (
            self.choices_shuffled
            if self.should_shuffle_choices
            else self.choices_ordered
        )
        return choices

    ##
    # Helpers

    def is_answered_by_user(self, user, check_correction=False):
        answers = user.answers.filter(choice__question=self)
        if check_correction:
            answers = answers.filter(choice__is_correct=True)
        is_answered = answers.exists()
        return is_answered
