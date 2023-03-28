from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Teste de URL para ver se fixo na mente")
