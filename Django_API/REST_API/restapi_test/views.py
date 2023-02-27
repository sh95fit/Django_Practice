from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapi_test.models import Addresses
from restapi_test.serializers import AddressesSerializer
from django.contrib.auth import authenticate

# Create your views here.

# 전체 조회


@csrf_exempt
def addresses_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# 개별 조회
@csrf_exempt
def addresses(request, pk):

    obj = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         search_name = data["name"]
#         obj = Addresses.objects.get(name=search_name)
#         print(obj.phone_number)

#         if data["phone_number"] == obj.phone_number:
#             return HttpResponse(status=200)
#         else:
#             return HttpResponse(status=400)

@csrf_exempt
def login(request):

    if request.method == "POST":
        print("request log :" + str(request.body))
        id = request.POST.get('userid', '')
        pw = request.POST.get('userpw', '')
        print("input id = " + id + " / input pw = " + pw)

        result = authenticate(username=id, password=pw)

        if result:
            print("로그인 성공")
            return HttpResponse(status=200)
        else:
            print("로그인 실패")
            return HttpResponse(status=401)
    return render(request, 'login.html')
