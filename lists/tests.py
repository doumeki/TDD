from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
import re
from lists.models import  Item


# Create your tests here.
class HomepageTest(TestCase):
    def test_root_url(self):
        found = resolve('/') #确发runserver?
        self.assertEqual(found.func,home_page)

    def test_home_page(self):
        request = HttpRequest()
        responese = home_page(request)
        self.assertTrue(responese.content.startswith(b'<html'))
        self.assertIn(b'<title>To-Do lists</title>',responese.content)
        self.assertTrue(responese.content.strip().endswith(b'</html>'))

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html',request=request)
        rep = self.remove_csrf(response.content.decode())
        expect_html = self.remove_csrf(expected_html)
        self.assertEqual(rep,expect_html)


    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        self.assertIn("A new list item", response.content.decode())
        expect_html = render_to_string('home.html',{'new_item_text':'A new list item'},request=request)
        rep = self.remove_csrf(response.content.decode())
        expect_html = self.remove_csrf(expect_html)
        self.assertEqual(rep,expect_html)

    @staticmethod
    def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_code)

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'Item the second')