from django.urls import path

from .views import AuthURL, IsAuthenticated

app_name = "Spotify"

urlpatterns = [
    path('get-auth', AuthURL.as_view(), name="GetAuth"),
    path('redirect', AuthURL.spotify_callback),
    path('authenticate', IsAuthenticated.as_view())
]
