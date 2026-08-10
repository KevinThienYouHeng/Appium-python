from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CheckoutComplete(BasePage):

    checkout_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/completeTV")
    thank_you_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/thankYouTV")
    green_statement = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/swagTV")
    continue_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/shoopingBt")

    def click_continue_button(self):
        self.click(*self.continue_button)