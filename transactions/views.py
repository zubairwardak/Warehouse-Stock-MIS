from django.shortcuts import render

from .models import (
    Receiving,
    Issue,
    Transfer,
    Return
)


def transaction_list(request):

    context = {

        "receiving":
            Receiving.objects.all().order_by('-id')[:10],


        "issues":
            Issue.objects.all().order_by('-id')[:10],


        "transfers":
            Transfer.objects.all().order_by('-id')[:10],


        "returns":
            Return.objects.all().order_by('-id')[:10],

    }


    return render(
        request,
        "transactions/transaction_list.html",
        context
    )