from django.db import models

# 장고의 내장 유저 모델을 사용하고 싶은 경우 (간단한 방법)
# from django.contrib.auth import get_user_model
# ID = get_user_model()

# 장고에서 내장 유저 모델을 사용하는 기본적인 방법
# AbstractUser : 모델을 django에서 미리 지정해둬 간편하게 가져와 사용 가능
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save


class CustomID (AbstractUser):
    pass  # AbstractUser을 그대로 사용할 경우


class UserProfile(models.Model):
    customer = models.OneToOneField(CustomID, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.username


# 모델 생성 시 ID는 django에서 자동 생성!
class Sale(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    # models.SET_NULL : Null로 변경하고 싶은 경우
    # models.SET_DEFAULT : 삭제 시 기본값으로 지정하고 싶은 경우

    # funnels_type = (
    #     ('naver', '네이버'),
    #     ('google', '구글'),
    #     ('news', '뉴스레터'),
    # )

    # 다양한 타입 형태 존재
    # is_existed = models.BooleanField(default=False)
    # funnels = models.CharField(choices=funnels_type, max_length=200)
    # your_images = models.ImageField(blank=True, null=True)
    # your_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Person(models.Model):
    customer = models.OneToOneField(CustomID, on_delete=models.CASCADE)
    groups = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.customer.username


def CreateUserProfileSignal(sender, instance, created, **kwargs):
    # print(instance, created)  # 어떤 정보가 오는지 확인 (created : 새로 생성되는 경우만 True 반환)
    if created:
        UserProfile.objects.create(customer=instance)


post_save.connect(CreateUserProfileSignal, sender=CustomID)
