from django.urls import path
from . import views

urlpatterns = [
    path('haha/', views.haha, name='haha'),
    path('lala/', views.lala, name='lala'),
    path('kaka/', views.kaka, name='kaka'),
]