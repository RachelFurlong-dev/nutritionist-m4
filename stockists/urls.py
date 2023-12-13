from django.urls import path
from . import views

# Define URL patterns for the stockists app
urlpatterns = [
    # Path for displaying the list of stockists
    path('', views.view_stockist_list, name='stockists'),
]
