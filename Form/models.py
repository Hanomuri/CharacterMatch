from django.db import models


# Create your models here.

class SeparatedValuesField(models.TextField):

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class FormQuestion(models.Model):
    question = models.CharField(max_length=200)
    answered = models.IntegerField(default=0)
    panswers = SeparatedValuesField("")
    answer = models.IntegerField(default=0)

class Character(models.Model):
    name = models.CharField(max_length=50)
    sexuals_orientations = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    migrant = models.BooleanField()
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    motto = models.CharField(max_length=200)
    mbti = models.CharField(max_length=10)
    neurodivergence = models.CharField(max_length=50)
    disability = models.CharField(max_length=40)
    kids = models.BooleanField()
    identity = models.CharField(max_length=50)
    







