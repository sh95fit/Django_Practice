from django.urls import path, include

from .views import Homepage, SalesList, SalesDetail, SaleInput, SaleUpdate, SaleDelete

app_name = "Sales"

urlpatterns = [
    path('', Homepage, name='Homepage'),
    path('sales', SalesList, name="List"),
    path('sales/<int:pk>', SalesDetail, name="Detail"),
    path('sales/make', SaleInput, name="Create"),
    path('sales/<int:pk>/update', SaleUpdate, name="Update"),
    path('sales/<int:pk>/delete', SaleDelete, name="Delete")
]
