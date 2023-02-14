from django.urls import path
from . import views

urlpatterns = [
    path('price/', views.price, name='price'),
    path('article/', views.article, name='article'),
    path('', views.index, name='index'),
]