from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('changer/', views.changer, name='changer'),
    path('detailretirer/', views.detailretirer, name='detailretirer'),
    path('retirer/', views.retirer, name='retirer'),
    path('detailajouter/', views.detailajouter, name='detailajouter'),
    path('ajouter/', views.ajouter, name='ajouter'),
]