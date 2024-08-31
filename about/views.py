from django.shortcuts import render, get_object_or_404
from .models import About
from .forms import CollaborateRequestForm


# Create your views here.

#class AboutList(generic.ListView):
#    queryset = About.objects.all()
#    template_name = "about/index.html"
#    paginate_by = 6
    
    # django automatically sets the context_object_name attribute to object_list.
    # e.g "about_list" is the context_object_name, this becomes our iterator
    # in the templates to show the about page
    # This is the class-based view for the about page.
    # It retrieves all About objects from the database
    
    
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
# This retrieves the most recent About object from the database
    collaborate_form = CollaborateRequestForm()
# This creates an instance of the CollaborateRequestForm form

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form,
         },
    )
# This renders the about page using the about.html template and passes the about object and collaborate_form form to the template
