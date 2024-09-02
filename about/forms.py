from django import forms
from .models import CollaborateRequest


class CollaborateRequestForm(forms.ModelForm):
    """
    A form that allows users to submit collaboration requests.

    **Context**
            
        ``CollaborateRequestForm``
                An instance of :model:`about.CollaborateRequest` that allows users to submit collaboration requests.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')

# The CollaborateRequestForm class is a ModelForm that allows users to submit collaboration requests in a nice easy looking form
# The Meta class inside the CollaborateRequestForm class tells Django which model to associate with the form
# CollaborateRequest is the model that handles the storage of collaboration requests in the database