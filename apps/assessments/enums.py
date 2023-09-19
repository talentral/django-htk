# HTK Imports
from htk.utils.enums import HtkEnum


class QuestionType(HtkEnum):
    UNSPECIFIED = 0
    # Answer is a free text response
    BASIC = 1
    # Multiple answer choices are presented, only one is correct
    MULTI_CHOICE = 2
    # Multiple answer choices are presented, any number (0 or many) can be correct,
    # all correct responses must be selected
    MULTI_CHOICE_MULTI_ANSWER = 4
