from django.db import models
from django.contrib.auth.models import User
# above imports the User model from django.contrib.auth.models as its built in to Django
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
# status choices for the Post model

# Create your models here.
class Post(models.Model):
    """
    Model definition for Post.

    Stores all the blog posts that users create. Related to the User model, so that each post
    has an author. :model:`auth.User`
        
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
        )
    # The author field is a foreign key that links to the User model. The on_delete parameter
    # specifies the behavior to adopt when the referenced object is deleted. CASCADE specifies
    # that when the user is deleted, also delete the blog posts associated with that user.
    featured_image = CloudinaryField('image', default='placeholder')
    # The featured_image field is a CloudinaryField that stores the URL of the blog image, instead of having to store the bulky image in the database.
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # This field uses the choices parameter to limit the available options for the status field to Draft
    # and Published.
    exerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_posted"]
    """
The Meta class provides additional information or metadata about the model. One of its options is ordering,
which specifies how the records associated with the model are ordered     
    """
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    #This method gives each post a name that superusers, rather than Python developers,
    # can more easily understand. When we look at posts in the console or admin panel,
    # this name helps us figure out which post is which.
    
    
class Comment(models.Model):
    """
    Model definition for Comment.

    Stores all the comments that users create on blog posts.
    Related to the Post and User models, :model:`blog.Post` :model:`auth.User`
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # The post field in the Comment model stores the ID of the blog post that a comment
    # is linked to. For example, if comments 1, 2 and 3 are all about Post 1, then they
    # will all have the same Foreign Key value of post = 1.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    content = models.TextField()
    approved = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'