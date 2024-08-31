from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # In the post_detail URL path, the argument value from the url tag is passed into <slug:slug>.
    # The slug path converter before the colon defines the data type as a slug, and the slug after the
    # colon is the post.slug value passed from the template. You see this value in the URL path in the
    # browser bar.
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    # In the comment_edit URL path, the argument value from the url tag is passed into <slug:slug> and <int:comment_id>.
    # The slug path converter before the colon defines the data type as a slug, and the slug after the colon is the post.slug value passed from the template.
    # You see this value in the URL path in the browser bar.
    # This identifies the post and comment to be edited.
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    # This identifies the post and comment to be deleted by passing the post.slug and comment.id values from the template.
]





"""
If you had a human resources web app that identified workers by their ID badge number, then you could use
the syntax <int:id_badge> to pass the integer argument to the URL path. Alternatively, a car mechanics web
app identifying cars by their alphanumeric registration plate could do so with <str:reg>.  
"""