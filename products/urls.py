from django.urls import path
from . import views

urlpatterns = [
   path("", views.index),
   path("saveDo", views.enter_task),
   path("home", views.home),
   path('login/login.html/', views.login),
   path('login/register.html/', views.register),
   path('dashboard/', views.dashboard),
   path('dashboard/productForm/', views.productForm),
   path('dashboard/productForm/newProduct', views.saveProduct),
   path('allproducts', views.showproducts),
]