from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import login

# Create your tests here.

class Testurls(SimpleTestCase):
    
    def test_login_url_resolves(self):
        url = reverse("account:login")
        #test whether the function taken from the resolved url is actually the same as the original function
        self.assertEquals(resolve(url).func, login)
