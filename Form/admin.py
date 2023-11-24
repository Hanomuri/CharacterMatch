from django.contrib import admin
from .models import FormQuestion
from .models import FQ
from .models import Character

# Register your models here.
admin.site.register(FormQuestion)
admin.site.register(FQ)
admin.site.register(Character)