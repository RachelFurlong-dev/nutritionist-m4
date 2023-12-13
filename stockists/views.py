from django.shortcuts import render
from .models import Stockist

# Import necessary modules and models for the views

# Define your views here


def view_stockist_list(request):
    # Retrieve all stockists from the database
    stockists = Stockist.objects.all()

    # Set the template file for rendering the stockist list
    template = 'stockists/stockist_list.html'

    # Prepare the context to be passed to the template
    context = {
        'stockists': stockists
    }

    # Render the template with the provided context
    return render(request, template, context)