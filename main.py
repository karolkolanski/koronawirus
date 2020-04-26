import unittest
from selenium import webdriver

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu")
        self.driver = webdriver.Firefox()

    def testSelenium(self):
        print("Test wlasciwy")
    def tearDown(self):
        print("sprzatanie po tescie")





