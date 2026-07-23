from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage

def test_click_login(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

def test_enter_username_only(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    assert login_page.get_username_value() == "standard_user"
    #login_page.login("standard_user", "secret_sauce")

def test_enter_password_only(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

    login_page = LoginPage(driver)
    login_page.enter_password("10203040")

def test_enter_credentials(driver):

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