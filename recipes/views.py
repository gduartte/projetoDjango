from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse("Home")
    return render(request, 'home.html')


def contato(request):
    return HttpResponse("Contato")

def sobre(request):
    return HttpResponse("Sobre")