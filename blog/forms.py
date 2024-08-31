from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        
# The CommentForm class is a ModelForm that allows users to submit comments on blog posts.
# The Meta class inside the CommentForm class tells Django which model to associate with the form
