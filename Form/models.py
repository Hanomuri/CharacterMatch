from django.db import models

# Create your models here.

class FormQuestion(models.Model):
    question = models.CharField(max_length=200)
    answered = models.IntegerField(default=0)