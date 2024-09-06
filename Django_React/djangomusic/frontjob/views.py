from django.shortcuts import render

# 접속 시 templates 하위 frontend 하위 index.html를 렌더링하도록 적용


def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
