from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class StudentList(APIView) :
    
    def get(self, request) :
        model = Student.objects.all()
        serializer = StudentSerializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid() :
            student = Student()
            student.student_id = request.data['student_id']
            student.name = request.data['name']
            student.age = request.data['age']
            student.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)