from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


# Create your tests here.
class HomepageTest(TestCase):
    def root_url(self):
        found = resolve('/') #确发runserver?
        self.assertEqual(found.func,home_page)
        print(found.func)

    def _home_page(self):
        request = HttpRequest()
        responese = home_page(request)
        print (responese.content)
        self.assertTrue(responese.content.startswith(b'<html'))
        self.assertIn(b'<title>To-Do lists</title>',responese.content)
        self.assertTrue(responese.content.strip().endswith(b'</html>'))

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content,expected_html)
