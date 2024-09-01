from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'about_table' # sets custom table name as default was about_about
    
    def __str__(self):
        return self.title
    
# This model is used to store the about page content in the database written through the admin interface.

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
    
# This is where every peice of information given by the user in the collaboarte form is collected and stored to allow users to submit collaboration requests
# This form will be used in the about_me view to handle the submission of collaboration requests.