from django.urls import path
from . import views

urlpatterns = [
    path('jaja/', views.krus, name='krus'),
    path('yaya/', views.pic, name='pic'),
    path('wawa/', views.bili, name='bili'),
]