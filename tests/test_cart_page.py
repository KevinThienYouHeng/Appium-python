from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage


def test_click_first_product(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_first_product()
    
    product_detail_page = ProductDetailPage(driver)
    assert product_detail_page.is_title_displayed()
    product_detail_page.click_add_to_cart()
    products_page.click_cart_button()

    cartPage = CartPage(driver)
    item = cartPage.get_total_item()
    print(f"Item: {item}")
    cartPage.click_checkout_button()

    loginPage = LoginPage(driver)
    loginPage.verify_login_page()

def test_click_increase_quantity(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_first_product()
    
    product_detail_page = ProductDetailPage(driver)
    assert product_detail_page.is_title_displayed()
    product_detail_page.click_add_to_cart()
    products_page.click_cart_button()

    cartPage = CartPage(driver)
    #cartPage.click_increase_item()
    cartPage.increase_first_item(2)
    quantity_item = cartPage.get_item_quantity()
    print(f"Quantity: {quantity_item}")

    