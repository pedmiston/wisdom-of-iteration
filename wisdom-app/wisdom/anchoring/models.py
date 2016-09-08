from django.db import models

from experiment.models import Experiment


class AnchoringExperiment(Experiment):
    name = models.CharField(max_length=80)
    text = models.TextField()
