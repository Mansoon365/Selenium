class LoginPage():
    def __init__(self,driver):
        self.driver= driver
        self.signing_button_xpath = "/html/body/div[1]/header/div/div[2]/div[2]/a[1]"
        self.username_textbox_id= "login_field"
        self.password_textbox_id = "password"
        self.login_button_name = "commit"

    def click_sign(self):
        self.driver.find_element_by_xpath(self.signing_button_xpath).click()

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys("Mansoon365")

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear
        self.driver.find_element_by_id(self.password_textbox_id).send_keys("Sisirr67")

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()