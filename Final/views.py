from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def home(request):
    return render(request, "home.html")

def lista(request):
        print(Person.objects.all())
        persons = Person.objects.all()
        return render(request, 'lista.html', {'persons': persons})