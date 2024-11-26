# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Booklist),
    path('add/',CreateBook),
    path('update/<int:id>/',UpdateBook),
    path('delete/<int:id>/',DeleteBook),
   
]