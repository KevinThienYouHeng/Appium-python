from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.dialog_page import DialogPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage
from pages.checkout_page_two import CheckoutPageTwo
from pages.base_page import BasePage
from pages.checkout_page_three import CheckoutPageThree

def test_reach_checkout_3_title(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.enter_full_credentials("Max","1234567812345","12/25","123")

    checkoutPageThree = CheckoutPageThree(driver)
    checkoutPageThree.verify_checkout_title_displayed()

    basePage = BasePage(driver)
    basePage.screenshot("checkout_page_3.png")

def test_get_total_items_checkout_3(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.enter_full_credentials("Max","1234567812345","12/25","123")

    checkoutPageThree = CheckoutPageThree(driver)
    total_items = checkoutPageThree.get_total_items()
    print(f"Total items: {total_items}")
    assert total_items == "Total items: 1"

def test_content_checkout_3(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.enter_full_credentials("Max","1234567812345","12/25","123")

    checkoutPageThree = CheckoutPageThree(driver)
    checkoutPageThree.verify_pages_header()

def test_click_payment(driver):
    checkoutPageTwo = CheckoutPageTwo(driver)
    checkoutPageTwo.reach_checkout_two_title()
    checkoutPageTwo.enter_full_credentials("Max","1234567812345","12/25","123")

    checkoutPageThree = CheckoutPageThree(driver)
    checkoutPageThree.click_payment_button()
