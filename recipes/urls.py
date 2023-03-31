from django.urls import path

from recipes.views import home

urlpatterns = [
    path('', home),
]

# path('ROTA_VIEW/', TEMPLATE.HTML)
# path('contato/', contato.html)
