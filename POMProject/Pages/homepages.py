class HomePage():
    def __init__(self,driver):
        self.driver=driver

        self.profile_link_xpath = "/html/body/div[1]/header/div[7]/details/summary"
        self.logout_button_xpath = "/html/body/div[1]/header/div[7]/details/details-menu/form/button"

    def click_summery(self):
        self.driver.find_element_by_xpath(self.profile_link_xpath) .click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()