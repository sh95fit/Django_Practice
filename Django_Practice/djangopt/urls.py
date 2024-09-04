from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("sales.urls", namespace="Sales")),
    # 로그인 성공 시 기본 리다이렉트 경로가 accounts/profile로 되어 있어 수정 필요! -> settings.py에서 설정
    path('login', LoginView.as_view(), name="Login"),
    path('logout', LogoutView.as_view(), name="Logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
