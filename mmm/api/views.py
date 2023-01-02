from django.shortcuts import render
from .models import Student
from .models import Teacher
from .models import Employee
from .serializer import studentSerializer
from .serializer import teacherSerializer
from .serializer import employeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {    
        '/List_student' : '/list_student',
        '/List_employee' : '/list_employee',
        '/List_teacher' : '/list_teacher',
        '/Delete_student' : '/delete_student',
        '/Delete_employee' : '/delete_employee',
        '/Delete_teacher' : '/delete_teacher',
        # '/Create' : '/create',
        # '/Update' : '/update',
    }

    return Response(api_urls)    

@api_view(['GET'])
def list_student(request):
    student = Student.objects.all()
    serializer = studentSerializer(student, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def list_teacher(request):
    teacher = Teacher.objects.all()
    serializer = teacherSerializer(teacher, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def list_employee(request):
    employee = Employee.objects.all()
    serializer = employeeSerializer(employee, many=True)

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()

    return Response(status= status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()

    return Response(status= status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()

    return Response(status= status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def create_student(request):
    serializer = studentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

@api_view(['POST'])
def create_teacher(request):
    serializer = teacherSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

@api_view(['POST'])
def create_employee(request):
    serializer = employeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)














# @api_view(['POST'])
# def create_student(request):
#     serializer = studentSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#         return Response(serializer.data)

# @api_view(['POST'])
# def update_student(request, pk):
#     student = Student.objects.get(pk=pk)
#     serializer = studentSerializer(instance=student, data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#         return Response(serializer.data)

# @api_view(['DELETE'])
# def delete_student(request, pk):
#     student = Student.objects.get(pk=pk)
#     student.delete()

#     return Response(status= status.HTTP_202_ACCEPTED)
