from django.test import TestCase
from .forms import CommentForm

# All of the test class method names must also begin with test_.
class TestCommentForm(TestCase):
   
    def test_form_is_valid(self):
        """ Test that the comment form is valid """
        comment_form = CommentForm({'content': 'This is a great post'})
# We create an instance of the CommentForm class with the content field set to 'This is a great post'.
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')
# We use the assertTrue method to check if the form is valid. If the form is valid, the test passes.
        
    def test_form_is_invalid(self):
        """ Test that the comment form is invalid """
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')