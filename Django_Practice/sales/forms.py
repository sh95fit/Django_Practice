from django import forms
from .models import Sale

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

# 모델 폼


class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            'first_name',
            'last_name',
            'age',
            'person'
        )


# 일반 폼
class SaleInputForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


User = get_user_model()
# 회원가입 폼 (커스터마이징 UserCreationForm)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
