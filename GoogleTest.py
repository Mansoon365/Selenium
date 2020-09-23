from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/mansoonupadhayaya/Downloads/chromedriver")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_searchautomation(self):
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_name("q").send_keys("Python for beginners")
        self.driver.find_element_by_id("search_button_homepage").click()

    def test_searchauto(self):
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_name("q").send_keys("selenium for beginners")
        self.driver.find_element_by_id("search_button_homepage").click()

    @classmethod
    def tearDownClass(cls):
        print("test completed")
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner =HtmlTestRunner.HTMLTestRunner (output="/Users/mansoonupadhayaya/Desktop") )