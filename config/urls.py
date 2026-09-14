from django.contrib import admin
from django.urls import path, include

from reports.views import dashboard


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'dashboard/',
        dashboard
    ),

    path(
        'inventory/',
        include('inventory.urls')
    ),

    path(
        'transactions/',
        include('transactions.urls')
    ),

    path(
        'reports/',
        include('reports.urls')
    ),

]