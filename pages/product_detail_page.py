from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    # Locators
    PRODUCT_TITLE = (AppiumBy.XPATH, "//*[@text='Sauce Labs Backpack']")
    PRICE = (AppiumBy.XPATH, "//*[@text='$ 29.99']")
    
    def is_title_displayed(self):
        return self.is_displayed(*self.PRODUCT_TITLE)
    
    def get_price(self):
        return self.get_text(*self.PRICE)