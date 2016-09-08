from django import forms

from .models import AnchoringExperiment


class NewGameForm(forms.ModelForm):
    class Meta:
        model = AnchoringExperiment
        fields = ['name', 'text']
