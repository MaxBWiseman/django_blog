from django.shortcuts import render, get_object_or_404
from django.contrib import messages
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
  
    if request.method == "POST":
# The first argument sent to any Django view function is the request object. Convention states that we give this parameter the name of request as well, for example:
# def about_me(request):
# That means that we can determine the HTTP verb that was used for our request by looking at the request.method property.
        print("Recieved a POST request")
        collaborate_form = CollaborateRequestForm(data=request.POST)
        if collaborate_form.is_valid():
# The is_valid() method makes sure we don't try to write a null value to the database. It also helps improve the security of our system
            collaborate_form.save()
# Now, we can finally call the save method to write the data to the database.
            messages.add_message(
                request, messages.SUCCESS,
                'Request submitted and I aim to respond within 24 hours.'
            )
#  When a prompt message is added, we then display it using the code we added below the nav in base.html.
    

    else:
        collaborate_form = CollaborateRequestForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form,
         },
    )
# This renders the about page using the about.html template and passes the about object and collaborate_form form to the template
