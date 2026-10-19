from django.urls import path
from prova_pratica_1_A.views import index, somma, media, voti

app_name="prova_pratica_1_A"
urlpatterns = [
    path('', index, name='index'),
    path('somma', somma, name='somma'),
    path('media', media, name='media'),
    path('voti', voti, name='voti'),
]