from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-date_posted")
    # This line of code tells Django to retrieve all posts with a status of 1 (published) and order them
    # by the created_on field in descending order.
    template_name = "blog/index.html"
    paginate_by = 6