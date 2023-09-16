from django.shortcuts import render
from .models import Stockist

# Create your views here.


def view_stockist_list(request):
    stockists = Stockist.object.all()
    context = {
        'stockists': stockists
    }
    return render(request, 'stockists/stockist_list.html', context)