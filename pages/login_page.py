from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
    USERNAME_ERROR_TEXT = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV")
    PASSWORD_ERROR_TEXT = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV")

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
    
    def is_username_error_displayed(self):
        return self.is_displayed(*self.USERNAME_ERROR_TEXT)
    
    def get_username_error_text(self):
        return self.get_text(*self.USERNAME_ERROR_TEXT)
    
    def is_password_error_displayed(self):
        return self.is_displayed(*self.PASSWORD_ERROR_TEXT)
    
    def get_password_error_text(self):
        return self.get_text(*self.PASSWORD_ERROR_TEXT)