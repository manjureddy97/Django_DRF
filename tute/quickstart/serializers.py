from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # Specify the model here
        fields = '__all__'  # Include all fields in the model
