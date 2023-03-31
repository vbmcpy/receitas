from django.http import HttpResponse
from django.shortcuts import render


# namespace recipes para o template
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Victor Bruno'})  # noqa: E501
