from django.shortcuts import render

from .models import *


def Home(request):
    Featur = feauters.objects.all()
    Fields = fields.objects.all()

    return render(request, 'Home.html', {'feature': Featur,'Fields':Fields,})


def Востребованность(request):
    graphic = Востребованно.objects.all()
    return render(request, 'Востребованность.html',{'graphic':graphic})


def География(request):
    grap = Географ.objects.all()
    return render(request, 'География.html',{'grap':grap})


def Навыки(request):
    return render(request, 'Навыки.html')


def Последниевакансии(request):
    return render(request, 'Последниевакансии.html')

# Create your views here.
