from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from products.models import Product

# Create your views here.

def reviews(request, product_id):
    """ A view to show all available reviews for current product """
    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product)
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'product': product,
    }
    return render(request, template, context)
