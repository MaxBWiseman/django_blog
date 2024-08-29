from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
]

# This is the URL configuration for the about app.
# It maps the root URL to the about_me view.