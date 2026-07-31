from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.cart_page import CartPage
import pytest

def test_click_first_product(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_first_product()
    
    product_detail_page = ProductDetailPage(driver)
    assert product_detail_page.is_title_displayed()

def test_click_catalog(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_catalog()
    products_page.get_first_product_name()
    #assert menu_page.is_catalog_visible()

def test_click_about(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_about()

def test_click_cart_icon(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_cart_button()

    cart_page = CartPage(driver)
    assert cart_page.is_no_items_displayed()
    

def test_click_product_cart(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_first_product()

    product_detail_page = ProductDetailPage(driver)
    product_detail_page.click_add_to_cart()
    #didn't click add to cart button
    products_page.click_cart_button()

    cart_page = CartPage(driver)
    assert cart_page.is_cart_displayed()

def test_current_cart_number(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.get_cart_count()

def test_click_cart_based_on_name(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_product_by_name('Sauce Labs Backpack (orange)')

    product_detail_page = ProductDetailPage(driver)
    product_detail_page.click_add_to_cart()
    driver.back()

    products_page.click_product_by_name('Sauce Labs Backpack (red)')
    product_detail_page.click_add_to_cart()
    products_page.click_menu_button()
    menu_page = MenuPage(driver)
    menu_page.click_catalog()
    
    cartNumber = products_page.get_cart_count()
    print(f"Cart Number: {cartNumber}")
    products_page.click_cart_button()

@pytest.mark.skip(reason="Not implemented yet")
def test_click_cart_based_on_onsie(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    #issue with the item itself, it breaks the app when click sauce labs onesie
    products_page.click_product_by_name('Sauce Labs Onesie')

def test_click_three_products_by_text(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_first_product()

    product_detail_page = ProductDetailPage(driver)
    product_detail_page.click_add_to_cart()
    driver.back()

    products_page.click_product_by_name('Sauce Labs Backpack (red)')
    product_detail_page.click_add_to_cart()
    driver.back()

    products_page.click_product_by_name('Sauce Labs Backpack (orange)')
    product_detail_page.click_add_to_cart()
    #driver.back()

    products_page.click_cart_button()

    cart_page = CartPage(driver)
    assert cart_page.is_cart_displayed()
    items = cart_page.get_total_item()
    print(f"Items: {items}")
    assert items == "3 Items"

def test_click_three_products_by_number(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_first_product()

    product_detail_page = ProductDetailPage(driver)
    product_detail_page.click_add_to_cart()
    driver.back()

    products_page.click_product_by_name('Sauce Labs Backpack (red)')
    product_detail_page.click_add_to_cart()
    driver.back()

    products_page.click_product_by_name('Sauce Labs Backpack (orange)')
    product_detail_page.click_add_to_cart()
    #driver.back()
    products_page.click_cart_button()

    cart_page = CartPage(driver)
    assert cart_page.is_cart_displayed()
    items = cart_page.get_number_total_item()
    assert items == 3
    print(f"Items: {items}")


