from django.shortcuts import render
from .serializers import BookSerializer
from .models import *  # Assuming the model is named `BooksModel`
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def Booklist(request):
    booksobj = BooksModal.objects.all()  # Queryset
    serializer = BookSerializer(booksobj, many=True)  # Serialize the queryset
    return Response(serializer.data)
