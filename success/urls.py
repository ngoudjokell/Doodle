from django.urls import path
from . import views

urlpatterns=[
    path('', views.success_view, name='success'),
    path('login/', views.success_view, name='login'),
]