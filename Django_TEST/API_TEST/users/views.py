from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from .models import User

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

def logout_view(request) :
    logout(request)
    return redirect("user:login")

def signup_view(request) :
    
    if request.method == "POST" :
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        pwd_id = request.POST["pwd_id"]
        
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.pwd_id = pwd_id
        user.save()
        return redirect("user:login")
    return render(request, "users/signup.html")