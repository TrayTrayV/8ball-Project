from django.db import models

# Create your models here.
class eightBallResponse(models.Model):
    classifier = models.CharField(max_length=15, blank=True)
    text = models.CharField(max_length=255)