from django.urls import path, include

from .views import Homepage, SalesList, SalesDetail, SaleInput, SaleUpdate, SaleDelete
from .views import HomepageView, SalesInputView, SalesListView, SalesDetailView, SalesUpdateView, SalesDeleteView

app_name = "Sales"

urlpatterns = [
    # path('', Homepage, name='Homepage'),  # 일반 함수 적용 형태
    path('', HomepageView.as_view(), name='Homepage'),  # 제너릭 뷰
    # path('sales', SalesList, name="List"),  # 일반 함수 적용 형태
    path('sales', SalesListView.as_view(), name="List"),  # 일반 함수 적용 형태
    # path('sales/<int:pk>', SalesDetail, name="Detail"), # 일반 함수 적용 형태
    path('sales/<int:pk>', SalesDetailView.as_view(), name="Detail"),  # 제너릭 뷰
    # path('sales/make', SaleInput, name="Create"), # 일반 함수 적용 형태
    path('sales/make', SalesInputView.as_view(), name="Create"),  # 제너릭 뷰
    # path('sales/<int:pk>/update', SaleUpdate, name="Update"), # 일반 함수 적용 형태
    path('sales/<int:pk>/update', SalesUpdateView.as_view(), name="Update"),  # 제너릭 뷰
    # path('sales/<int:pk>/delete', SaleDelete, name="Delete"), # 일반 함수 적용 형태
    path('sales/<int:pk>/delete', SalesDeleteView.as_view(), name="Delete"),  # 제너릭 뷰
]
