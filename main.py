import unittest
from selenium import webdriver

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.sukienkimm.pl/")
        self.driver.maximize_window()

    def testSelenium(self):
        driver = self.driver
        print("Klikam zaloguj sie")
        zaloguj_btn = driver.find_element_by_xpath('//span[text()=" zaloguj się"]')
        zaloguj_btn.click()

    def tearDown(self):
        print("sprzatanie po tescie")
        self.driver.quit()






