from django.shortcuts import render, redirect, reverse
from rest_framework import generics, status

from .serializer import MusicRoomSerializer, CreateRoomSerializer
from .models import MusicRoom

from rest_framework.views import APIView
from rest_framework.response import Response


class MusicRoomView(generics.ListAPIView):
    queryset = MusicRoom.objects.all()
    serializer_class = MusicRoomSerializer


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            vote_to_skip = serializer.data.get('vote_to_skip')
            host = self.request.session.session_key

            queryset = MusicRoom.objects.filter(host=host)

            if queryset.exists():
                musicRoom = queryset[0]
                musicRoom.guest_can_pause = guest_can_pause
                musicRoom.vote_to_skip = vote_to_skip

                musicRoom.save(
                    update_fields=['guest_can_pause', 'vote_to_skip'])

                return Response(MusicRoomSerializer(musicRoom).data, status=status.HTTP_200_OK)
            else:
                musicRoom = MusicRoom(
                    host=host, guest_can_pause=guest_can_pause, vote_to_skip=vote_to_skip)

                musicRoom.save()

                return Response(MusicRoomSerializer(musicRoom).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
