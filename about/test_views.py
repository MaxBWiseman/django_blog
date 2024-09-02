from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateRequestForm
from .models import About

class TestAboutViews(TestCase):
    def setUp(self):
        self.about = About(title="About title", content="About content")
# We create an instance of the About model with the title and content fields
# set to "About title" and "About content
        self.about.save()
# We save the instance of the About model to the test database.

    def test_render_about_detail_page_with_collaborate_request_form(self):
        """ Test that the about view renders the about page with the collaborate request form """
        response = self.client.get(reverse('about'))
# We use self.client.get() with this URL to send a GET request to the about view.
        self.assertEqual(response.status_code, 200)
# The status code 200 means that the request was successful. If the status code is 404,
# then the page was not found.
        self.assertIn(b"About title", response.content)
# The assertIn method checks if the text "About title" is in the response content.
        self.assertIn(b"About content", response.content)
# The assertIn method checks if the text "About content" is in the response content.
        self.assertIsInstance(
            response.context['collaborate_request_form'], CollaborateRequestForm)
# Verifies that the collaborate_request_form from the about view's context is an
# instance of the CollaborateRequestForm class.

    def test_successful_collaborate_request_submission(self):
        """ Test for submitting a collaboration request"""
        post_data = {
            'name': 'Test Name',
            'email': 'test@test.com',
            'message': 'Test message'
        }
# We create a dictionary called post_data with the keys 'name', 'email', and 'message'.
# This is our fake data for the test.
        response = self.client.post(reverse('about'), post_data)
# We use self.client.post() to send a POST request to the about view with the post_data dictionary
        self.assertEqual(response.status_code, 200)
# The status code 200 means that the request was successful.
        self.assertIn(
            b'Request submitted and I aim to respond within 24 hours.',
            response.content
        )
# The assertIn method checks if the message text 'Request submitted and I aim to respond within 24 hours.'
# pops up in the response content (the HTML of the page).
        