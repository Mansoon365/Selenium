from selenium import webdriver
import time
import unittest

import HtmlTestRunner
from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.homepages import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/mansoonupadhayaya/Downloads/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://github.com/")
        login = LoginPage(driver)
        login.click_sign()
        login.enter_username("Mansoon365")
        login.enter_password("Sisirr67")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_summery()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        print("Test Completed")
        cls.driver.close()
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/Users/mansoonupadhayaya/Desktop"))