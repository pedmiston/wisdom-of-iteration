from django.db import models


class Experiment(models.Model):
    class Meta:
        abstract = True
