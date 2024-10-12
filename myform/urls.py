from django.urls import path
from . import views
urlpatterns=[
    path('',views.contact,name='name'),
    path('success/', views.contact, name='success')
]