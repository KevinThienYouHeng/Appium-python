from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class Products(BasePage):

    PRODUCTS_TITLE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    FIRST_PRODUCT_IMAGE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    FIRST_PRODUCT_NAME = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
    MENU_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV")
    cart_badge = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartTV")
    cart_icon = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartRL")


    def wait_for_products_screen(self):
        self.find(*self.PRODUCTS_TITLE)

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT_IMAGE)

    def get_first_product_name(self):
        return self.get_text(*self.FIRST_PRODUCT_NAME)
    
    def click_menu_button(self):
        self.click(*self.MENU_BUTTON)

    def click_cart_button(self):
        self.click(*self.cart_icon)

    def get_cart_count(self):
        try:
            return self.get_text(*self.cart_badge)
        except:
            return 0