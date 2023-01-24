from django.urls import path
from . import views


urlspatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),    
]