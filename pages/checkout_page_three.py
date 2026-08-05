from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage

class CheckoutPageThree(BasePage):

    #titleObjects
    checkout_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/checkoutTitleTV")
    DELIVER_ADDRESS_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Deliver Address"]')
    PAYMENT_METHOD_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Payment Method"]')
    DHL_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/dhlTV")

    item_displays = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/placeOrderRV")
    total_items = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemNumberTV")
    total_amount = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalAmountTV")
    payment_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")

    def verify_checkout_title_displayed(self):
        return self.is_displayed(*self.checkout_title)

    def get_total_items(self):
        return self.get_text(*self.total_items)

    def verify_pages_header(self):
        headers = {
            "Deliver Address": self.DELIVER_ADDRESS_HEADER,
            "Payment Method": self.PAYMENT_METHOD_HEADER,
        }

        for name, locator in headers.items():
            element = self.find(*locator)
            assert element.is_displayed(), f"'{name}' header is not displayed"

        return self

    def click_payment_button(self):
        self.click(*self.payment_button)


