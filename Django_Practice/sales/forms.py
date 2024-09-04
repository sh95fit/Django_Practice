from django import forms
from .models import Sale


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
