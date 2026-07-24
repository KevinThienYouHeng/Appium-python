from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CartPage(BasePage):

    no_items_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noItemTitleTV")
    cart_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    proceed_checkout_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    image_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    item_name = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
    item_price = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV")
    decrease_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV")
    increase_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV")
    remove_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/removeBt")



    def is_no_items_displayed(self):
        return self.is_displayed(*self.no_items_title)

    def is_cart_displayed(self):
        return self.is_displayed(*self.cart_title)