from django.http import HttpResponse
from django.shortcuts import render


# name space recipes para o template
def home(request):
    return render(request, 'recipes/home.html')
