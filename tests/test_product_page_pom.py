from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage


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

