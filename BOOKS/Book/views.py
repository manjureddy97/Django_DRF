from django.shortcuts import render
from .serializers import BookSerializer
from .models import BooksModal  # Ensure correct import of the model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

# Read
@api_view(['GET'])
def Booklist(request):
    booksobj = BooksModal.objects.all()  # Queryset
    serializer = BookSerializer(booksobj, many=True)  # Serialize the queryset
    return Response(serializer.data)

# Create
@api_view(['POST'])
def CreateBook(request):  # Renamed function to CreateBook
    # Instantiate the serializer with data from the request
    serializer = BookSerializer(data=request.data)
    
    if serializer.is_valid():  # Check if the data is valid
        # Save the new book instance
        serializer.save()
        return Response(serializer.data, status=201)  # Return the serialized data with status 201 (Created)
    else:
        return Response(serializer.errors, status=400)  # Return validation errors with status 400 (Bad Request)
    
# Update
@api_view(['PUT'])
def UpdateBook(request, id):
    try:
        bookobj = BooksModal.objects.get(id=id)  # Check if the book exists
    except BooksModal.DoesNotExist:
        raise NotFound("Book not found")

    serializer = BookSerializer(bookobj, data=request.data)  # Corrected the serializer instantiation
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
    
    #delete
@api_view(['DELETE'])
def DeleteBook(request, id):
    try:
        bookobj = BooksModal.objects.get(id=id)
    except BooksModal.DoesNotExist:
        raise NotFound("Book not found")
    bookobj.delete()
    return Response('Book is deleted',status=204)  # Return status 204 (No Content) after successful deletion
