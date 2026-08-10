from pages.checkout_page_two import CheckoutPageTwo
from pages.base_page import BasePage

def test_reach_checkout_2_title(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()

def test_enter_fullname_checkout_2(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.enter_full_name("John Doe")
    checkoutPageTwo.click_review_order_button()

def test_enter_full_credentials_checkout_2(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.enter_full_name("John Doe")
    checkoutPageTwo.enter_card_number("4111111111111111")
    checkoutPageTwo.enter_expiration_date("12/25")
    checkoutPageTwo.enter_security_code("123")
    checkoutPageTwo.click_review_order_button()

def test_verify_all_error_displayed_checkout_2(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.click_review_order_button()
    assert checkoutPageTwo.verify_all_error_displayed()

def test_verify_name_error_displayed_checkout_2(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.enter_card_number("4111111111111111")
    checkoutPageTwo.enter_expiration_date("12/25")
    checkoutPageTwo.enter_security_code("123")
    checkoutPageTwo.click_review_order_button()
    assert checkoutPageTwo.verify_full_name_error()

def test_verify_payment_icon_displayed(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.verify_payment_icons_displayed()
    basePage = BasePage(driver)
    basePage.screenshot("checkout_page_2.png")