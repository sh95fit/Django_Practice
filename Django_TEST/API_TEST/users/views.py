from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse

# Create your views here.
def login_view(request) :
    if request.method == "POST" :
        # print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None :
            print("로그인 성공")
            login(request, user)
            # return HttpResponse(status=200)
        else :
            print("로그인 실패")
            # return HttpResponse(status=401)
    return render(request, "users/login.html")