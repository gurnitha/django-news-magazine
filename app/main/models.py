# app/main/models.py

# Import django/third parties modules
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name