# myapp/serializers.py
from rest_framework import serializers
from .models import StudentData

class StudentSerializer(serializers.ModelSerializer):
    total_score = serializers.ReadOnlyField()

    class Meta:
        model = StudentData
        fields = '__all__'
