from django.test import TestCase

class HomeTest(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_includes_links_to_experiments(self):
        response = self.client.get('/')
        self.assertRegexpMatches(response.content.decode(), 'id_anchoring')
