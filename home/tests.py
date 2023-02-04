from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, redirect_index

# Create your tests here.

class Testurls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("home:index")
        
        self.assertEquals(resolve(url).func, index)

    def text_redirect_index_url_resolves(self):
        url = reverse("home:redirect_index")
        
        self.assertEquals(resolve(url).func, redirect_index)
