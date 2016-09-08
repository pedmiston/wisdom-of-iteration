from django.shortcuts import render
from django.views.generic import CreateView

from .forms import NewGameForm


def home(request):
    return render(request, 'anchoring/home.html')


class NewGame(CreateView):
    form_class = NewGameForm
    template_name = 'anchoring/new.html'
