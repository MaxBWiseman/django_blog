from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form that allows users to submit comments on blog posts.

    **Context**
        
    ``CommentForm``
            An instance of :model:`blog.Comment` that allows users to submit comments on blog posts.
    **Template:**
        :template:`blog/post_detail.html`
    """
    class Meta:
        model = Comment
        fields = ('content',)
        
# The CommentForm class is a ModelForm that allows users to submit comments on blog posts.
# The Meta class inside the CommentForm class tells Django which model to associate with the form
