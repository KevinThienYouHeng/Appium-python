from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")

    def login(self, username, password):
        self.find(*self.USERNAME_FIELD).send_keys(username)
        self.find(*self.PASSWORD_FIELD).send_keys(password)
        self.find(*self.LOGIN_BUTTON).click()

    def enter_username(self, username):
        self.find(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
            self.find(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.find(*self.LOGIN_BUTTON).click()

    def get_username_value(self):
        return self.find(*self.USERNAME_FIELD).get_attribute("text")
    
    def get_password_value(self):
        return self.find(*self.PASSWORD_FIELD).get_attribute("text")