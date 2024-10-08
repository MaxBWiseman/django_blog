from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class PostAdmin(SummernoteModelAdmin):
    """
    django_summernote is a plugin that allows us to use the Summernote in the admin panel.

    **Context**
    
    ``PostAdmin``
        An instance of :model:`about.About` that represents the About model in the Django admin interface.
    
    """

    summernote_fields = ('content',)


# Register your models here.

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
    
# This is where we register the models with the admin panel
# so that we can manage them through the admin interface.