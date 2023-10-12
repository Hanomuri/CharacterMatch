from django.db import models

# Create your models here.

class FormQuestion(models.Model):
    question = models.CharField(max_length=200)
    answered = models.IntegerField(default=0)

class Character(models.Model):
    name = models.CharField(max_length=50)
    sexuals_orientations = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50)
    job = models.CharField(max_length=40)
    migrant = models.BooleanField()
    age = models.IntegerField()
    country = models.CharField(max_length=15)
    motto = models.CharField(max_length=200)
    mbti = models.CharField(max_length=10)
    neurodivergence = models.CharField(max_length=50)
    disability = models.CharField(max_length=40)
    kids = models.BooleanField()
    identity = models.CharField(max_length=50)
    







