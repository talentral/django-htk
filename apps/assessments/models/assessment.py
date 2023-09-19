# HTK Imports
from htk.models.classes import HtkBaseModel


class Assessment(HtkBaseModel):
    class Meta:
        verbose_name = 'Assessment'

    @property
    def max_score(self):
        return self.questions.count()
