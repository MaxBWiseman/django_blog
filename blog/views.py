from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-date_posted")
    # This line of code tells Django to retrieve all posts with a status of 1 (published) and order them
    # by the created_on field in descending order.
    template_name = "blog/index.html"
    paginate_by = 6
    
    # django automatically sets the context_object_name attribute to object_list.
    # e.g "post_list" is the context_object_name, this becomes our iterator
    # in the templates to show all published posts in order of date posted.
    
    
def post_detail(request, slug):
# two parameters:
# request: The HTTP request object.
# slug: A string representing the slug of the post to be displayed.
# The slug parameter gets the argument value from the URL pattern named post_detail. Inside urls.py
# The slug value is unique, so only one post in the database matches this argument.
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
# This filters the Post model objects to include only those with a status of 1 (Published).
# The result is stored in the queryset variable.
    post = get_object_or_404(queryset, slug=slug)
# This function attempts to retrieve a single Post object from the queryset where the slug
# matches the provided slug parameter. If no such object exists, it raises a 404 Not Found error.
    comments = post.comments.all().order_by("-date_posted")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
        
    comment_form = CommentForm()
    
    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )
"""
This renders the blog/post_detail.html template with the context containing the post object. 
The render function takes three arguments:

request: The HTTP request object.

"blog/post_detail.html": The path to the template to be rendered.

{"post": post}: A dictionary containing the context data to be passed to the template.
In this case, it includes the post object. the object was being passed to the template as a
Python dictionary, we retrieved one single blog post, stored it in a variable
called post and passed that through to the template in a dictionary where both the value and key
name was, you guessed it, post. This is called context and it is how you pass data from your own views
to a template.

In our view, above, we select a single blog post from the database, the one whose slug matches the slug
in our URL. We store that result in a variable called post, and then we add a dictionary as an argument
to the render function. This dictionary is referred to as context. It is convention that the key
name would be the same as the variable name we're passing through, e.g. {"post": post}.
"""