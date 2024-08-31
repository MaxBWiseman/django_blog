from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'about_table' # sets custom table name as default was about_about
    
    def __str__(self):
        return self.title
    
# This model is used to store the about page content in the database.

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
    
# This model is used to store collaboration requests in the database. The read field is used to track whether the request has been read or not.
# The __str__ method is used to return a string representation of the object. In this case, it returns the name of the person who submitted the request.