from django.urls import path
from . import views

# this urls.py is created by me to redirect the url.py in the main  crm folder here

urlpatterns = [
    path('',views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]