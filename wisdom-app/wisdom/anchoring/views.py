from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from experiment.views import ExperimentList
from .models import AnchoringExperiment
from .forms import NewGameForm


class Home(ExperimentList):
    template_name = 'anchoring/home.html'
    model = AnchoringExperiment


class NewGame(CreateView):
    template_name = 'anchoring/new.html'
    form_class = NewGameForm

    def get_success_url(self):
        return reverse('anchoring:home')
