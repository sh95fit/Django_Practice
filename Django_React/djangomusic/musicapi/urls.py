from django.urls import path

from .views import MusicRoomView

app_name = "Music"

urlpatterns = [
    path('', MusicRoomView.as_view(), name="RootAPI"),
]
