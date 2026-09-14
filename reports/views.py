from django.shortcuts import render

from inventory.models import Item, Stock
from warehouses.models import Warehouse
from transactions.models import Receiving, Issue



def dashboard(request):

    total_stock = 0

    for stock in Stock.objects.all():
        total_stock += stock.quantity


    context = {

        "total_warehouses":
            Warehouse.objects.count(),


        "total_items":
            Item.objects.count(),


        "total_stock":
            total_stock,


        "total_receiving":
            Receiving.objects.count(),


        "total_issue":
            Issue.objects.count(),

    }


    return render(
        request,
        "reports/dashboard.html",
        context
    )