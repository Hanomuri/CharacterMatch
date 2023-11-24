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
    answer = models.IntegerField(default=0)


yesono = [["Yes", "Yes"],["No", "No"]]
likely = [[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"]]
one_choices = [('Gay', 'Gay'), 
            ('Bisexual', 'Bisexual'), 
            ('Lesbiana', 'Lesbiana'), 
            ('Asexual', 'Asexual'),
            ('Arromantico', 'Arromantico'),
            ('Pansexual', 'Pansexual'),
            ('Sin etiqueta', 'Sin etiqueta'),
            ('Otra', 'Otra')
            ]
two_choices = [['Trastorno limite de personalidad', 'Trastorno limite de personalidad'], 
            ['Autismo', 'Autismo'], 
            ['TDAH', 'TDAH'], 
            ['Dislexia', 'Dislexia'], 
            ['Sindrome de Tourette', 'Sindrome de Tourette'], 
            ['Otra', 'Otra']]
three_choices = [['ESTJ', 'ESTJ'], ['ISTJ', 'ISTJ'], ['ISFJ', 'ISFJ'], ['ESFJ', 'ESFJ'], ['INTP', 'INTP'], ['ENTP', 'ENTP'], ['INTJ', 'INTJ'], ['ENTJ', 'ENTJ'], ['ESFP', 'ESFP'], ['ISFP', 'ISFP'], ['ESTP', 'ESTP'], ['ISTP', 'ISTP'], ['ENFJ', 'ENFJ'], ['INFJ', 'INFJ'], ['INFP', 'INFP'], ['ENFP', 'ENFP']]
four_choices = [['Blanca', 'Blanca'], ['Mestiza', 'Mestiza'], ['Afroamericana', 'Afroamericana'], ['Asiática', 'Asiática']]
five_choices = [['SININFORMACION', 'SININFORMACION']]
six_choices = [['Masculino', 'Masculino'], ['Femenino', 'Femenino'], ['Queer', 'Queer'], ['No binarie', 'No binarie'], ['Sin etiquetas', 'Sin etiquetas']]
seven_choices = [['Reino Unido', 'Reino Unido'], ['Estados Unidos', 'Estados Unidos'], ['Argentina', 'Argentina'], ['Chile', 'Chile'], ['Australia', 'Australia'], ['Libano', 'Libano'], ['Sudáfrica', 'Sudáfrica'], ['Canadá', 'Canadá'], ['Italia', 'Italia'], ['Tanzania', 'Tanzania'], ['España', 'España'], ['Republica Dominicana', 'Republica Dominicana'], ['Puerto Rico', 'Puerto Rico'], ['otro', 'otro']]

"""
4)    Que Etnia posees?
Posibles Respuestas: Blanco, Blanca, Mestiza, Mestizo, Afroamericano, Afroamericana, Asiático, Asiática 
5)    Posees alguna discapacidad?
Posibles respuestas: me dedicare a buscarlas XD
6)    Te sientes mas comodx con personajes o personas?
7)    Con cual genero te identificas?:
Posibles respuestas: Masculino, Femenino, Queer, No binarie, Sin etiquetas.
8)    Eres una persona trans?
Posibles respuestas: Si/No
9)    En que país Naciste?
Posibles Respuestas: Reino Unido, Estados Unidos, Argentina, Chile, Australia, Libano, Sudáfrica, Canadá, Italia, Tanzania, España, Republica Dominicana, Puerto Rico, otro.
no se si estas de acuerdo con esas preguntas, si es que gustas puedo intentar pensar en otras
"""

class FQ(models.Model):
    name = models.CharField(max_length=50, default="None")
    sexuality = models.CharField(max_length=50, default="None", choices=one_choices)
    neurodivergence = models.CharField(max_length=50, default="None", choices=two_choices)
    mbti = models.CharField(max_length=10, default="None", choices=three_choices)
    ethnicity = models.CharField(max_length=50, default="None", choices=four_choices)
    disability = models.CharField(max_length=50, default="None", choices=five_choices)
    confort = models.IntegerField(default=0, choices=likely)
    identity = models.CharField(max_length=50, default="None", choices=six_choices)
    trans = models.CharField(max_length=4, default="None", choices=yesono)
    country = models.CharField(max_length=30, default="None",choices=seven_choices)
    def __str__(self):
        return self.name

    def __sex__(self):
        return self.sexuality
    
    def __neuro__(self):
        return self.neurodivergence

    def __mbti__(self):
        return self.mbti

    def __ethnicity__(self):
        return self.ethnicity

    def __disability__(self):
        return self.disability

    def __confort__(self):
        return self.confort

    def __ident__(self):
        return self.identity
    
    def __trans__(self):
        return self.trans
    
    def __country__(self):
        return self.country
    
    



class Character(models.Model):
    name = models.CharField(max_length=50)
    sexuality = models.CharField(max_length=50)
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
    
    def __str__(self):
        return self.name







