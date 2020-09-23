from selenium import webdriver
import time
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("/Users/mansoonupadhayaya/Downloads/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        print("test completed")
        driver.close()
        driver.quit()


    def test_search(self,test_setup):
        driver.get("https://duckduckgo.com/")
        driver.find_element_by_name("q").send_keys("Python for beginners")
        driver.find_element_by_id("search_button_homepage").click()
        time.sleep(10)

# def test_teardown():
#     print("test completed")
#     driver.close()
#     driver.quit()

# if __name__ == "__main__":
#     unittest.main()