from django.urls import path

from .views import index

app_name = "Front"

urlpatterns = [
    path('', index, name="HomePage"),
    path('join', index),
    path('create', index),
    path('room/<str:roomTitle>', index),
]
