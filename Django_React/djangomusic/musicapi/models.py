from django.db import models


# 음악 방의 이름을 랜덤하게 만들어주도록하는 함수
import string
import random


def generate_unique_title():
    length = 5

    while True:
        title = ''.join(random.choices(string.ascii_uppercase, k=length))
        if MusicRoom.objects.filter(title=title).count() == 0:
            break
    return title


# 음악 방
class MusicRoom(models.Model):
    title = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    vote_to_skip = models.IntegerField(null=False, default=1)
    create_dates = models.DateTimeField(auto_now_add=True)
