from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    # Locators
    PRODUCT_TITLE = (AppiumBy.XPATH, "//*[@text='Sauce Labs Backpack']")
    PRICE = (AppiumBy.XPATH, "//*[@text='$ 29.99']")
    add_to_cart_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    
    def is_title_displayed(self):
        return self.is_displayed(*self.PRODUCT_TITLE)
    
    def get_price(self):
        return self.get_text(*self.PRICE)

    def click_add_to_cart(self):
        self.click(*self.add_to_cart_button)