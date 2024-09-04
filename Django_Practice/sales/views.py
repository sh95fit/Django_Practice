from django.shortcuts import render
from django.http import HttpResponse

from .models import CustomID


def Homepage(request):
    customer = CustomID.objects.all()
    context = {
        "MenuName": "Noodle",
        "Price": "10,000 won",
        "Customer": customer
    }
    return render(request, "sales/index.html", context)
