from rest_framework import serializers

from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BooksModal
        fields='__all__'