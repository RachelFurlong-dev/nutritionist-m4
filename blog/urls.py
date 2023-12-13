from django.urls import path
from . import views

# Define URL patterns for the blog app
urlpatterns = [
    # Path for displaying the list of posts
    path('', views.PostList.as_view(), name='post_list'),

    # Path for displaying the details of a specific post identified by its slug
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
