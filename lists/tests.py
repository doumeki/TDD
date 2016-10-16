from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest


# Create your tests here.
class HomepageTest(TestCase):
    def test_root_url(self):
        found = resolve('/') #确发runserver?
        #self.assertEqual(found.func,home_page)
        print(found.func)

    def test_home_page(self):
        request = HttpRequest()
        responese = home_page(request)
        self.assertTrue(responese.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-DO lists</title>',responese.content)
        self.assertTrue(responese.content.endswith(b'</html>'))