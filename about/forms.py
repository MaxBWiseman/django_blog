from .models import CollaborateRequest
from django import forms


class CollaborateRequestForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')

# The CollaborateRequestForm class is a ModelForm that allows users to submit collaboration requests.
# The Meta class inside the CollaborateRequestForm class tells Django which model to associate with the form