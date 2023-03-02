from django.urls import path, include
from student.api import StudentList

urlpatterns = [
    path('api/student_list', StudentList.as_view(), name='student_list'),
]