from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
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

                self.request.session['room_title'] = musicRoom.title

                return Response(MusicRoomSerializer(musicRoom).data, status=status.HTTP_200_OK)
            else:
                musicRoom = MusicRoom(
                    host=host, guest_can_pause=guest_can_pause, vote_to_skip=vote_to_skip)

                musicRoom.save()

                return Response(MusicRoomSerializer(musicRoom).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class GetRoom(APIView):
    serializer_class = MusicRoomSerializer
    lookup_url_kwarg = 'title'

    def get(self, request, format=None):
        title = request.GET.get(self.lookup_url_kwarg)
        if title != None:
            room = MusicRoom.objects.filter(title=title)
            if len(room) > 0:
                data = MusicRoomSerializer(room[0]).data
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({"invalid room": "Wrong room name..."}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Incorrect Request': "Incorrect Request..."}, status=status.HTTP_400_BAD_REQUEST)


class JoinRoom(APIView):
    lookup_url_kwarg = 'title'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        title = request.data.get(self.lookup_url_kwarg)

        if title != None:
            room_result = MusicRoom.objects.filter(title=title)
            if len(room_result) > 0:
                room = room_result[0]
                self.request.session['room_title'] = title
                return Response({"message": "Access the Room"}, status=status.HTTP_200_OK)

            return Response({"Bad Request": "Wrong Room number..."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"Bad Request": "Wrong Information..."}, status=status.HTTP_400_BAD_REQUEST)


class UserInRoom(APIView):
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        data = {
            'title': self.request.session.get("room_title")
        }

        return JsonResponse(data, status=status.HTTP_200_OK)
