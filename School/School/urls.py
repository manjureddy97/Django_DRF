from django.contrib import admin
from django.urls import path
from SchoolApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.StudentList.as_view()),  # All students
    path('add/', views.CreateStudent.as_view()),  # Create student
    path('rev/<int:pk>/', views.RetrieveStudent.as_view()),  # Retrieve single student by pk
    path('update/<int:pk>/', views.UpdateStudent.as_view()),  # Update student
    path('delete/<int:pk>/', views.DeleteStudent.as_view()),  # Delete student
]
