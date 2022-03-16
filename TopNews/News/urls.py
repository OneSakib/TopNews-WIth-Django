from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statewise', views.statewise, name='statewise')
]
