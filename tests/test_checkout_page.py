from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.dialog_page import DialogPage
#from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage

def test_enter_checkout_longWay(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("10203040")
    login_page.click_login_button()

    products_page.click_first_product()
    product_detail_page = ProductDetailPage(driver)
    product_detail_page.click_add_to_cart()
    #didn't click add to cart button
    products_page.click_cart_button()

    cartPage = CartPage(driver)
    cartPage.click_checkout_button()

    checkoutPage = CheckoutPage(driver)
    title = checkoutPage.get_checkout_title()
    print(f"Checkout title: {title}")
    assert checkoutPage.is_checkout_title_displayed()

def test_reach_checkout_title(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    title = checkoutPage.get_checkout_title()
    print(f"Checkout title: {title}")
    assert checkoutPage.is_checkout_title_displayed()

def test_checkout_credentials(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    checkoutPage.enter_full_name("John Doe")
    checkoutPage.enter_address_line1("123 Main St")
    checkoutPage.enter_city("Anytown")
    checkoutPage.enter_zip_code("12345")
    checkoutPage.enter_state("CA")
    checkoutPage.enter_country("USA")
    checkoutPage.click_payment_button()

def test_verify_checkout_page(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    checkoutPage.verify_checkout_page()

def test_verify_full_name(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    assert checkoutPage.verify_full_name_field()

def test_checkout_error_message_name(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    checkoutPage.click_payment_button()
    checkoutPage.verify_field_error_icon(checkoutPage.full_name_parent, "Full Name")
    checkoutPage.verify_full_name_error_message()

def test_checkout_error_message_address(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    checkoutPage.click_payment_button()
    checkoutPage.verify_field_error_icon(checkoutPage.address_line1_parent, "Address Line 1")
    checkoutPage.verify_field_error(checkoutPage.address_line1_error, "Please provide your address.")

def test_checkout_error_message_city(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    checkoutPage.click_payment_button()
    checkoutPage.verify_field_error_icon(checkoutPage.city_item_parent, "City")
    checkoutPage.verify_field_error(checkoutPage.city_item_error, "Please provide your city.")

def test_checkout_error_message_zipCode(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    checkoutPage.click_payment_button()
    checkoutPage.verify_field_error_icon(checkoutPage.zip_code_parent, "Zip Code")
    checkoutPage.verify_field_error(checkoutPage.zip_code_error, "Please provide your zip")

def test_checkout_error_message_country(driver):
    checkoutPage = CheckoutPage(driver)
    checkoutPage.reach_checkout_title()
    checkoutPage.click_payment_button()
    checkoutPage.verify_field_error_icon(checkoutPage.country_item_parent, "Country")
    checkoutPage.verify_field_error(checkoutPage.country_item_error, "Please provide your")


    