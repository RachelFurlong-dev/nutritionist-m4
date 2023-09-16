from django.shortcuts import render
from .models import Stockist

# Create your views here.


def view_stockist_list(request):
    stockists = Stockist.objects.all()
    template = 'stockists/stockist_list.html'
    context = {
        'stockists': stockists
    }
    return render(request, template, context)