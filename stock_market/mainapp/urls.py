
from django.urls import path
from mainapp import views
urlpatterns = [
    path('',views.getNifty50List,name="get_nifty_50_list"),
    path('getStockDetails',views.getStockdetails,name="get_stock_detail")
]
