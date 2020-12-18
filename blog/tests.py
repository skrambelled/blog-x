from django.test import TestCase
from django.urls import reverse

class BlogTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('blog/home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_page_template(self):
        url = reverse('blog/home')tell 
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'blog/home.html')
        self.assertTemplateUsed(res, '_base.html')
        