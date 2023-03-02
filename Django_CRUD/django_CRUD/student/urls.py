from django.urls import path, include
from student.api import StudentList, StudentDetail

urlpatterns = [
    path('api/student_list', StudentList.as_view(), name='student_list'),
    path('api/student_list/<int:student_id>', StudentDetail.as_view(), name='student_list')
]