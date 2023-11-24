from django.shortcuts import render, HttpResponse
from .forms import FormQuestions
from .models import FQ, Character
from django.http import HttpResponseRedirect
from random import randint

# Create your views here.

def home(request):
    return render(request, "home.html")

def faq(request):
    return render(request, "faq.html")

def form(request):
    submitted = False
    if request.method == "POST":
        form = FormQuestions(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/form?submitted=True")
    else:
        form = FormQuestions
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, "form.html", {"f": form, "submitted": submitted})

def result(request):
    sexuality = "None"
    ndiver = "None"
    mbti = "None"
    ethnicity = "None"
    disability = "None"
    identity = "None"
    country = "None"

    get = False
    if request.method == "POST":
        result_name = request.POST.get("name")
        FQ_i = FQ.objects.all().filter(name=result_name)
        
        for i in FQ_i:
            sexuality = Character.objects.all().filter(sexuality=i.__sex__())
            ndiver = Character.objects.all().filter(neurodivergence=i.__neuro__())
            mbti = Character.objects.all().filter(mbti=i.__mbti__())
            ethnicity = Character.objects.all().filter(ethnicity=i.__ethnicity__())
            disability = Character.objects.all().filter(disability=i.__disability__())
            identity = Character.objects.all().filter(identity=i.__ident__())
            country = Character.objects.all().filter(country=i.__country__())
            
            if(sexuality.__len__() == 0):
                sexuality = "None"
            else:
                a = randint(0, sexuality.__len__()-1)
                sexuality = sexuality[a].__str__()
            
            if(ndiver.__len__() == 0):
                ndiver = "None"
            else:
                a = randint(0, ndiver.__len__()-1)
                ndiver = ndiver[a].__str__()

            if(mbti.__len__() == 0):
                mbti = "None"
            else:
                a = randint(0, mbti.__len__()-1)
                mbti = mbti[a].__str__()

            if(ethnicity.__len__() == 0):
                ethnicity = "None"
            else:
                a = randint(0, ethnicity.__len__()-1)
                ethnicity = ethnicity[a].__str__()
            
            if(disability.__len__() == 0):
                disability = "None"
            else:
                a = randint(0, disability.__len__()-1)
                disability = disability[a].__str__()

            if(identity.__len__() == 0):
                identity = "None"
            else:
                a = randint(0, identity.__len__()-1)
                identity = identity[a].__str__()      

            if(country.__len__() == 0):
                country = "None"
            else:
                a = randint(0, country.__len__()-1)
                country = country[a].__str__()         
        get = True
    else:
        result_name = FQ.objects.all()

    return render(request, "result.html", {"names": result_name, 
                                           "get": get,
                                           "sex": sexuality,
                                           "ndiver": ndiver,
                                           "mbti": mbti,
                                            "ethn": ethnicity,
                                            "disa": disability,
                                            "iden": identity,
                                            "country": country
                                           })

  