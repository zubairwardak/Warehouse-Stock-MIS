from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.report_home,
        name="report_home"
    ),

    path(
        'stock/',
        views.stock_report,
        name="stock_report"
    ),

    path(
        'low-stock/',
        views.low_stock_report,
        name="low_stock_report"
    ),

]