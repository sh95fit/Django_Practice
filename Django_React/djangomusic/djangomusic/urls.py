from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # namespace 설정 시 해당 urls.py에 app_name이 설정되어 있어야한다!
    path('', include("musicapi.urls", namespace="Music")),
]
