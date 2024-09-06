from django.shortcuts import render
from rest_framework import generics

from .serializer import MusicRoomSerializer
from .models import MusicRoom


class MusicRoomView(generics.ListAPIView):
    queryset = MusicRoom.objects.all()
    serializer_class = MusicRoomSerializer
