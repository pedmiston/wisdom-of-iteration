from django.test import TestCase
from django.urls import reverse

from anchoring.forms import NewGameForm

class AnchoringTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url_home = reverse('anchoring:home')
        cls.url_new = reverse('anchoring:new')

    def test_anchoring_page_renders_anchoring_template(self):
        response = self.client.get(self.url_home)
        self.assertTemplateUsed(response, 'anchoring/home.html')

    def test_anchoring_page_includes_link_to_create_experiment_form(self):
        response = self.client.get(self.url_home)
        self.assertRegexpMatches(response.content.decode(), 'id_new')

    def test_new_game_page_contains_new_game_form(self):
        response = self.client.get(self.url_new)
        form = response.context['form']
        self.assertIsInstance(form, NewGameForm)
