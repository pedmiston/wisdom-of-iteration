from django.test import TestCase
from django.urls import reverse

class HomeTest(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_includes_links_to_experiments(self):
        response = self.client.get('/')
        self.assertRegexpMatches(response.content.decode(), 'id_anchoring')

class AnchoringTest(HomeTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.anchoring_url = reverse('anchoring')

    def test_anchoring_page_renders_anchoring_template(self):
        response = self.client.get(self.anchoring_url)
        self.assertTemplateUsed(response, 'home_pages/anchoring.html')

    def test_anchoring_page_includes_link_to_create_experiment_form(self):
        response = self.client.get(self.anchoring_url)
        self.assertRegexpMatches(response.content.decode(), 'id_new')
