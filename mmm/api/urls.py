from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('', views.apiOverview, name='api_overviews'),
    path('listStudent/', views.list_student, name='ListStudent'),
    path('listTeacher/', views.list_student, name='ListTeacher'),
    path('listEmployee/', views.list_student, name='ListEmployee'),
    path('deleteStudent/<str:pk>/', views.delete_student, name='DeleteStudent'),
    path('deleteTeacher/<str:pk>/', views.delete_teacher, name='DeleteTeacher'),
    path('deleteEmployee/<str:pk>/', views.delete_employee, name='DeleteEmployee'),
    path('createStudent/', views.create_student, name='CreateStudent'),
    path('createEmployee/', views.create_employee, name='CreateEmployee'),
    path('createTeacher/', views.create_teacher, name='CreateTeacher'),
    # path('update/<str:pk>/', views.update_student, name='UpdateStudent'),
]
