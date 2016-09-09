from django.shortcuts import render
from django.views.generic import CreateView

from experiment.views import ExperimentList
from .models import AnchoringExperiment
from .forms import NewGameForm


class Home(ExperimentList):
    template_name = 'anchoring/home.html'
    model = AnchoringExperiment


class NewGame(CreateView):
    form_class = NewGameForm
    template_name = 'anchoring/new.html'
