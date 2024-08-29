from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

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
    
    
def about_detail(request, slug):
    """
    Display an individual :model:`about.About`.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """
    queryset = About.objects.first()
    about = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "about/about.html",
        {"about": about},
    )
# This renders the about/about_detail.html template with the context containing the
# about object, instead of a class-based view, this is a function-based view