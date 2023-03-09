# from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet

from .models import Info

from .serializer import InfoSerializer


# Create your views here.
class InfoViewSet(ModelViewSet) :
  queryset = Info.objects.all()
  serializer_class = InfoSerializer


# REST Framework를 사용하지 않는 경우
# def index(request) :
#   # model_to_dict
#   # list(Student.objects.values())

#   # s_list = Info.objects.all()
#   s_list = []

#   for s in Info.objects.all() :
#     s_list.append({
#       'name': s.name,
#       'email': s.email,
#       'rating': s.rating
#     })

  # return JsonResponse(s_list, safe=False)