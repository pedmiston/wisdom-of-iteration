from django.test import TestCase
from django.urls import reverse

class AnchoringTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.anchoring_url = reverse('anchoring')

    def test_anchoring_page_renders_anchoring_template(self):
        response = self.client.get(self.anchoring_url)
        self.assertTemplateUsed(response, 'anchoring/home.html')

    def test_anchoring_page_includes_link_to_create_experiment_form(self):
        response = self.client.get(self.anchoring_url)
        self.assertRegexpMatches(response.content.decode(), 'id_new')
