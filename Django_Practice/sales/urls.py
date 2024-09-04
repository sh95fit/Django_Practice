from django.urls import path, include

from .views import Homepage, SalesList, SalesDetail, SaleInput, SaleUpdate, SaleDelete

app_name = "Sales"

urlpatterns = [
    path('', Homepage),
    path('sales', SalesList),
    path('sales/<int:pk>', SalesDetail),
    path('sales/make', SaleInput),
    path('sales/<int:pk>/update', SaleUpdate),
    path('sales/<int:pk>/delete', SaleDelete)
]
