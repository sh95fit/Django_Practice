from rest_framework import serializers
from .models import MusicRoom


class MusicRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicRoom
        fields = ('id', 'title', 'host', 'guest_can_pause',
                  'vote_to_skip', 'create_dates')


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicRoom
        fields = ('guest_can_pause', 'vote_to_skip')


class UpdateRoomSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[])

    class Meta:
        model = MusicRoom
        fields = ("guest_can_pause", "vote_to_skip", "title")
