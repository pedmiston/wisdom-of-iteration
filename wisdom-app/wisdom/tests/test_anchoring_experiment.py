from . import SeleniumTest

class AnchoringExperimentTest(SeleniumTest):
    def setUp(self):
        self.browser.get(self.live_server_url)

    def test_create_a_new_anchoring_experiment(self):
        """Create a new anchoring experiment via a web form."""

        # Navigate to form
        self.browser.find_element_by_id('id_anchoring').click()
        self.browser.find_element_by_id('id_new').click()

        # Fill out form
        experiment_name = 'test-anchoring-experiment'
        question_text = 'how many stars in the sky'
        form = self.browser.find_element_by_tag_name('form')
        form.find_element_by_id('id_name').send_keys(experiment_name)
        form.find_element_by_id('id_text').send_keys(question_text)
        form.find_element_by_name('submit').click()

        # Verify new experiment
        experiments = (self.browser.find_element_by_id('id_experiment_list')
                                   .find_elements_by_tag_name('li'))
        self.assertEquals(len(experiments), 1)
        self.assertEquals(experiments[0].text, experiment_name)
