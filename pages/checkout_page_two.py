from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage

class CheckoutPageTwo(BasePage):

    checkout_two_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV")
    full_name_input = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    card_number_input = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")
    expiration_date_input = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET")
    security_code_input = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET")
    checkbox_terms = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/billingAddressCB")
    review_order_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
    visa_icon = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/visaIV")
    mastercard_icon = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/mastercardIV")
    question_icon = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/questionIV")

    #errorObjects
    full_name_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV")
    expiration_date_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateErrorTV")
    security_code_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeErrorTV")



    def verify_checkout_two_title_displayed(self):
        return self.is_displayed(*self.checkout_two_title)

    def reach_checkout_two_title(self):
        checkoutPage = CheckoutPage(self.driver)
        checkoutPage.reach_checkout_title()
        checkoutPage.reach_checkout_page_two()
        self.verify_checkout_two_title_displayed()

    def enter_full_name(self, full_name):
        self.find(*self.full_name_input).send_keys(full_name)

    def enter_card_number(self, card_number):
        self.find(*self.card_number_input).send_keys(card_number)

    def enter_expiration_date(self, expiration_date):
        self.find(*self.expiration_date_input).send_keys(expiration_date)

    def enter_security_code(self, security_code):
        self.find(*self.security_code_input).send_keys(security_code)

    def click_checkbox_terms(self):
        self.click(*self.checkbox_terms)

    def click_review_order_button(self):
        self.click(*self.review_order_button)

    def verify_all_error_displayed(self):
        return (self.is_displayed(*self.full_name_error) and
                self.is_displayed(*self.expiration_date_error) and
                self.is_displayed(*self.security_code_error))

    def verify_full_name_error(self):
        return self.is_displayed(*self.full_name_error)

    def verify_expiration_date_error(self):
        return self.is_displayed(*self.expiration_date_error)

    def verify_security_code_error(self):
        return self.is_displayed(*self.security_code_error)

    def verify_payment_icons_displayed(self):
        visa = self.find(*self.visa_icon)
        mastercard = self.find(*self.mastercard_icon)

        assert visa.is_displayed(), "Visa icon is not displayed"
        assert mastercard.is_displayed(), "Mastercard icon is not displayed"

    def enter_full_credentials(self, full_name, card_number, expiration_date, security_code):
        self.enter_full_name(full_name)
        self.enter_card_number(card_number)
        self.enter_expiration_date(expiration_date)
        self.enter_security_code(security_code)
        self.click_review_order_button()
    

    
