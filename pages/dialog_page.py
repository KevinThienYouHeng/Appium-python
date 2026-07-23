from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DialogPage(BasePage):
    # Logout dialog
    DIALOG_TITLE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/alertTitle")
    DIALOG_MESSAGE = (AppiumBy.ID, "android:id/message")
    CANCEL_BUTTON = (AppiumBy.ID, "android:id/button2")
    LOGOUT_BUTTON = (AppiumBy.ID, "android:id/button1")

    def click_cancel_button(self):
        self.click(*self.CANCEL_BUTTON)

    def click_logout_button(self):
        self.click(*self.LOGOUT_BUTTON)

    def is_dialog_displayed(self):
        return self.is_displayed(*self.DIALOG_TITLE)
    
    def get_dialog_title(self):
        return self.get_text(*self.DIALOG_TITLE)
    
    def get_dialog_message(self):
        return self.get_text(*self.DIALOG_MESSAGE)