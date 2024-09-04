from django.shortcuts import render
from django.http import HttpResponse

from .models import CustomID, Sale


def Homepage(request):
    customer = CustomID.objects.all()
    context = {
        "MenuName": "Noodle",
        "Price": "10,000 won",
        "Customer": customer
    }
    return render(request, "sales/index.html", context)


def SalesList(request):
    sales = Sale.objects.all()

    sale_context = {
        "key": sales
    }

    return render(request, "sales/sales_list.html", sale_context)


def SalesDetail(request, pk):
    sale = Sale.objects.get(id=pk)
    detail_context = {
        "info": sale
    }
    # return HttpResponse(f"Detail Page - {sale.first_name} {sale.last_name}")
    return render(request, "sales/sales_detail.html", detail_context)
