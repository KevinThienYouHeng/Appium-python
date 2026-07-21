from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage


def test_click_first_product(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_first_product()
    
    product_detail_page = ProductDetailPage(driver)
    assert product_detail_page.is_title_displayed()