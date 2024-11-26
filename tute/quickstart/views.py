from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import  GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.
# @api_view(['GET'])
# def home(request):
#     student_obj = Student.objects.all()  # Correct this line
#     serializer = StudentSerializer(student_obj, many=True)
#     return Response({'status': 200, "payload": serializer.data})


# @api_view(['GET'])
# def post_student(request):
#      if(request.method=='GET'):
#          serializer=StudentSerializer(data=request.data)
#          if serializer.is_valid():  # Return succes
#              return Response({'status': 201, 'payload': serializer.data})  # Return success
#          return Response({'status': 400, 'errors': serializer.errors})  # Return error


## MIXINS
class Studentlist(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request):
        return self.list(request)
    
class Studentcreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request):
        return self.create(request)
    
class Studentretrive(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    
class Studentupdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    
class Studentdelete(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)

