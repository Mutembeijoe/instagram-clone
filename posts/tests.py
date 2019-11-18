from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class PostTest(TestCase):
   
    def test_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        #Rdirect expected due to login
        self.assertTemplateUsed('home.html')