from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage

class CheckoutComplete(BasePage):

    checkout_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/completeTV")
    thank_you_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/thankYouTV")
    green_statement = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/swagTV")
    continue_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/shoopingBt")

    def click_continue_button(self):
        self.click(*self.continue_button)