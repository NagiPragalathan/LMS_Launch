from django.db import models
from django.utils import timezone

# Create your models here.

class Toggle(models.Model):
    name = models.CharField(max_length=50)