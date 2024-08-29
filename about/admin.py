from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'updated_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.

admin.site.register(About)
