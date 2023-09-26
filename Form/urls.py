from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("faq/", views.faq, name="Faq"),
    path("form/", views.form, name="Form")
]