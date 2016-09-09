from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from .models import AnchoringExperiment


class NewGameForm(forms.ModelForm):
    class Meta:
        model = AnchoringExperiment
        fields = ['name', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create'))
