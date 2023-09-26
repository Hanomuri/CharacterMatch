from django.shortcuts import render, HttpResponse
from .models import FormQuestion

# Create your views here.

def home(request):
    return render(request, "home.html")

def faq(request):
    return render(request, "faq.html")

def form(request):
    questions = FormQuestion.objects.all()
    return render(request, "form.html", {"form": questions})