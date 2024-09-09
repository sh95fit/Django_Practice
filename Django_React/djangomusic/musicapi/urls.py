from django.urls import path

from .views import MusicRoomView, CreateRoomView, GetRoom

app_name = "Music"

urlpatterns = [
    path('', MusicRoomView.as_view(), name="RootAPI"),
    path('create', CreateRoomView.as_view(), name="Create"),
    path('get', GetRoom.as_view(), name="GetRoom"),
]
