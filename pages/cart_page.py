from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import re

class CartPage(BasePage):

    no_items_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noItemTitleTV")
    cart_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    proceed_checkout_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    image_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    item_name = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
    item_price = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV")
    decrease_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV")
    item_quantity = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV")
    increase_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV")
    remove_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/removeBt")
    total_price = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalPriceTV")
    total_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemsTV")


    def is_no_items_displayed(self):
        return self.is_displayed(*self.no_items_title)

    def is_cart_displayed(self):
        return self.is_displayed(*self.cart_title)

    def get_total_item(self):
        return self.get_text(*self.total_item)

    def get_number_total_item(self) -> int:

        total_item = self.find(*self.total_item)
        text = total_item.text
        match = re.search(r'\d+', text)
        if match:
            return int(match.group())
        raise ValueError(f"No number found in element text: {text}")

    def click_checkout_button(self):
        self.click(*self.proceed_checkout_button)

    def click_increase_item(self):
        self.click(*self.increase_item)

    def click_decrease_item(self):
        self.click(*self.decrease_item)

    def get_item_quantity(self):
        return self.get_text(*self.item_quantity)

    def increase_first_item(self, times: int):

        if times <= 0:
            return self

        for _ in range(times):
            self.click_increase_item()

        return self