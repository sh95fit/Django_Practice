from django.urls import path, include

from .views import Homepage, SalesList, SalesDetail, SaleInput

app_name = "Sales"

urlpatterns = [
    path('', Homepage),
    path('sales', SalesList),
    path('sales/<int:pk>', SalesDetail),
    path('sales/make', SaleInput),
]
