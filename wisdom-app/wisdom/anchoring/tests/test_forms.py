from django.test import TestCase

from anchoring.forms import NewGameForm

class FormTest(TestCase):
    def test_create_anchoring_game_via_form(self):
        data = dict(
            name='Original Anchoring Game',
            text='What percentage of the UN is African countries?',
        )
        form = NewGameForm(data)
        self.assertTrue(form.is_valid(), form.errors)
