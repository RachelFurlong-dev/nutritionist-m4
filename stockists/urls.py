from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stockist_list, name='stockists'),
]