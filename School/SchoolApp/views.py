from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.exceptions import NotFound

# Get all students
class StudentList(ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

# Create a student
class CreateStudent(CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

# Retrieve a student by id
class RetrieveStudent(RetrieveAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

    # def get_object(self):
    #     # Override get_object to filter by id from URL
    #     return get_object_or_404(StudentModel, pk=self.kwargs['pk'])

# Update a student
class UpdateStudent(UpdateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

# Delete a student
class DeleteStudent(DestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
