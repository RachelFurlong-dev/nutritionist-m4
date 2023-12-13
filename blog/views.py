from django.views import generic
from .models import Post

# Import necessary modules and models for the views

# Define your views here


class PostList(generic.ListView):
    # Specify the queryset for retrieving published posts ordered by publish date
    queryset = Post.objects.filter(status=1).order_by('-publish_date')

    # Specify the template file for rendering the post list
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    # Specify the model for retrieving details of a specific post
    model = Post

    # Specify the template file for rendering the post detail
    template_name = 'blog/post_detail.html'

