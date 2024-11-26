from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()  # Correct this line
    serializer = StudentSerializer(student_obj, many=True)
    return Response({'status': 200, "payload": serializer.data})


@api_view(['GET'])
def post_student(request):
     if(request.method=='GET'):
         serializer=StudentSerializer(data=request.data)
         if serializer.is_valid():  # Return succes
             return Response({'status': 201, 'payload': serializer.data})  # Return success
         return Response({'status': 400, 'errors': serializer.errors})  # Return error
