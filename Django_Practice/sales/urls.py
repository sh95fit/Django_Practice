from django.urls import path, include

from .views import Homepage

urlpatterns = [
    path('', Homepage)
]
