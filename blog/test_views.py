from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):
    """
self references the current class instance. It is used to create and access
variables that belong to that class.

In the context of testing, especially with Django's TestCase class, self is used
in the setUp method to create instance variables you want to use across different test methods.
And then, inside our test methods, we can access these variables to run our tests.     
    """
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", exerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()
    """
The setUp method is a special method we can use in our tests to provide initial
settings for our tests to use. In this case, we create a superuser and a small
blog post in our test database. This data is then assigned as a variable of the self object.
Pretty much creating fake data for our tests to use.     
    """

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
# Only need to provide a value for args if the URL you are building in reverse expects them. You can check
# in urls.py to see if the URL expect args.
# We use self.client.get() with this URL to send a GET request to the post_detail view.
# The reverse function generates a URL from a view name and its arguments. In this case,
# we are generating the URL for the post_detail view and passing the slug of the post we
# created in the setUp method.
        self.assertEqual(response.status_code, 200)
# The status code 200 means that the request was successful. If the status code is 404, then the
# page was not found.
        self.assertIn(b"Blog title", response.content)
# The assertIn method checks if the text "Blog title" is in the response content. The b before the string
# indicates that the string is in bytes format.verifying that our view correctly displays the blog post.
        self.assertIn(b"Blog content", response.content)
# The assertIn method checks if the text "Blog content" is in the response content.
# verifying that our view correctly displays the blog post.
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)
# Verifies that the comment_form from the post_detail view's context is an instance of the CommentForm class.
    """ 
To run our post_detail view, we need an instance of Post to render. As an instance of Post requires a
ForeignKey to a User for its author field, we first needed to create a superuser to author the blog post:
author=self.user.    
    """