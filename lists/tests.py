from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


# Create your tests here.
class HomepageTest(TestCase):
    def test_root_url(self):
        found = resolve('/') #确发runserver?
        self.assertEqual(found.func,home_page)
        print(found.func)

    def test_home_page(self):
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
        print(repr(response.content))
        self.assertEqual(response.content.decode(),expected_html)

    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        self.assertIn("A new list item", response.content.decode())
        expect_html = render_to_string('home.html',{'new_item_text':'A new list item'})
        print(expect_html)
        self.assertEqual(response.content.decode(),expect_html)
