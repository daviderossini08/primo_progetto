from django.urls import path
from .views import home, articoloDetailView, lista_articoli, queryBase, index

app_name="news"

urlpatterns = [
   path('', index, name="index"),
   path('homepage/', home, name="homeviews"),
   path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
   path("lista_articoli/<int:giornalista_id>", lista_articoli, name = "lista_articoli"),
   path('query_base/', queryBase, name='query_base'),
]