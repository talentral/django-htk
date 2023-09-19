# HTK Imports
from htk.apps.assessments.enums import QuestionType
from htk.utils.enums import get_enum_choices


def get_question_type_choices(include_hidden=True):
    choices = get_enum_choices(QuestionType, include_hidden=include_hidden)
    return choices
