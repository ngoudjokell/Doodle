from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.connecter, name='connecter'),
    path('admin/', views.connecter, name='admin'),
]



