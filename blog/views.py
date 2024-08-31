from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
# While the Post model doesn't have a field named comments, the related_name in our
# comment model sets up a logical link, effectively creating this association
    comment_count = post.comments.filter(approved=True).count()
# So, when we use post.comments.all(), it will return all comments related to the
# selected post by using related_name="comments". This is what is called a reverse
# lookup. We don't access the Comment model directly. Instead, we fetch the related
# data from the perspective of the Post model.

    
    if request.method == "POST":
# The first argument sent to any Django view function is the request object. Convention states that we give this parameter the name of request as well, for example:
# def post_detail(request, slug):
# That means that we can determine the HTTP verb that was used for our request by looking at the request.method property.
        print("Recieved a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
# The is_valid() method makes sure we don't try to write a null value to the database. It also helps improve the security of our system
            comment = comment_form.save(commit=False)
# Calling the save method with commit=False returns an object that hasn't yet been saved to the database so that we can modify it further.
# The object will not be written to the database until we call the save method again.
# We do this because we need to populate the post and author fields before we save.
            comment.author = request.user
# We can then modify the object by setting the author field of the comment to the current request.user - the user who is currently logged in.
            comment.post = post
# We also set the post field using the post variable, which contains the result of the get_object_or_404 helper function at the start of the view code.
            comment.save()
# Now, we can finally call the save method to write the data to the database.
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
# This function accepts a request, a message tag, which we will use to style the messages later, and message text. When a message is added, we then display it using the code we added below the nav in base.html.
        
    comment_form = CommentForm()
# Outside the if statement, we create a blank instance of the CommentForm class. This line resets the content of the form to blank so that a user can write a second comment if they wish.
    
    print("About to render template")
    
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
# This filters the Post model objects to include only those with a status of 1 (Published).
        post = get_object_or_404(queryset, slug=slug)
# This function attempts to retrieve a single Post object from the queryset where the slug matches the provided slug parameter. If no such object exists, it raises a 404 Not Found error.
        comment = get_object_or_404(Comment, pk=comment_id)
# This function attempts to retrieve a single Comment object from the queryset where the pk matches the provided comment_id parameter. If no such object exists, it raises a 404 Not Found error.
        comment_form = CommentForm(data=request.POST, instance=comment)
# The instance argument is used to specify the instance of the Comment model that we want to edit. This instance is retrieved from the database using the get_object_or_404 function.

        if comment_form.is_valid() and comment.author == request.user:
# The is_valid() method makes sure we don't try to write a null value to the database. It also helps improve the security of our system
            comment = comment_form.save(commit=False)
# Calling the save method with commit=False returns an object that hasn't yet been saved to the database so that we can modify it further.
            comment.post = post
# We also set the post field using the post variable, which contains the result of the get_object_or_404 helper function at the start of the view code.
            comment.approved = False
# We also set the approved field to False so that the comment has to be approved by an admin before it is displayed.
            comment.save()
# Now, we can finally call the save method to write the data to the database
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
# Sends a message to the user if the form is not valid.
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
# This view returns you to the post webpage after you've edited the comment. This return is done with a HttpResponseRedirect and reverse to refresh the post_detail view.


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)
# This function attempts to retrieve a single Comment object from the queryset where the pk matches the provided comment_id parameter.
# If no such object exists, it raises a 404 Not Found error.

    if comment.author == request.user:
# This checks if the author of the comment is the same as the user who is currently logged in.
        comment.delete()
# If the author of the comment is the same as the user who is currently logged in, the comment is deleted.
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
# Prompt message if the user tries to delete a comment that is not theirs or successfully deletes their comment.
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
# This view returns you to the post webpage after you've deleted the comment. This return is done with a HttpResponseRedirect
# and reverse to refresh the post_detail view.