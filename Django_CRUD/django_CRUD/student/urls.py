from django.urls import path, include
from student.api import StudentList, StudentDetail

# 토큰 받아오기
from rest_framework.authtoken import views

urlpatterns = [
    path('api/student_list', StudentList.as_view(), name='student_list'),
    path('api/student_list/<int:student_id>', StudentDetail.as_view(), name='student_list'),
    path('api/auth', views.obtain_auth_token, name='obtain_auth_token'),
]