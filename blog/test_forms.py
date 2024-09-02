from django.test import TestCase
from .forms import CommentForm

# All of the test class method names must also begin with test_.
class TestCommentForm(TestCase):
    """
    Test class for the CommentForm form.The TestCase import is Django's testing
    library, which allows us to define tests using a class-based approach.
    creates an instance of our CommentForm and fills out the body field of
    the form with a string - This is a great post. A dictionary with the field
    as the key and the content as the value is used. A form with more fields
    would have a matching number of key:value pairs.
    Finally, it uses an assert to determine if the form is valid.

    Args:
        TestCase (_type_): _description_
    """

    def test_form_is_valid(self):
        comment_form = CommentForm({'content': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is valid')
        
    def test_form_is_invalid(self):
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is not valid')