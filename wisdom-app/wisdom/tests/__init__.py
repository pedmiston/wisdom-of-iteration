from selenium import webdriver
from django.test import LiveServerTestCase

class SeleniumTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        super().tearDownClass()
