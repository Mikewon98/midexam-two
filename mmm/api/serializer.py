from rest_framework import serializers
from .models import Student
from .models import Teacher
from .models import Employee

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__' 

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' 