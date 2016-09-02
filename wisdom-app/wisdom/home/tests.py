from django.test import TestCase
from django.urls import reverse

class HomeTest(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_includes_links_to_experiments(self):
        response = self.client.get('/')
        self.assertRegexpMatches(response.content.decode(), 'id_anchoring')

    def test_anchoring_page_renders_anchoring_template(self):
        anchoring_url = reverse('anchoring')
        response = self.client.get(anchoring_url)
        self.assertTemplateUsed(response, 'home_pages/anchoring.html')
