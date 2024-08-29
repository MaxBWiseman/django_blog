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