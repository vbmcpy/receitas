from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]

# path('ROTA_VIEW/', TEMPLATE.HTML)
# path('contato/', contato.html)
