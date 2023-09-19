# HTK Imports
from htk.apps.assessments.models.fk_fields import (
    fk_assessment,
    fk_question,
)
from htk.models.classes import HtkBaseModel


DEFAULT_RELATED_NAME = 'responses'


class AssessmentResponse(HtkBaseModel):
    assessment = fk_assessment(DEFAULT_RELATED_NAME, required=True)
    question = fk_question(DEFAULT_RELATED_NAME, required=True)

    class Meta:
        verbose_name = 'Assessment Question Response'
