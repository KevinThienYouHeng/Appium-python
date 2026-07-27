from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.dialog_page import DialogPage

def test_click_login(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

def test_click_loginbutton(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

    login_page = LoginPage(driver)
    login_page.click_login_button()
    #login_page.is_username_error_displayed()
    assert login_page.is_username_error_displayed()
    assert login_page.get_username_error_text() == "Username is required"
    print(login_page.get_username_error_text())

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

def test_enter_username_only_click_button(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    assert login_page.get_username_value() == "standard_user"
    login_page.click_login_button()
    #login_page.is_password_error_displayed()
    assert login_page.is_password_error_displayed()
    assert login_page.get_password_error_text() == "Enter Password"
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
    login_page.click_login_button()
    assert login_page.is_username_error_displayed()
    assert login_page.get_username_error_text() == "Username is required"

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

def test_logout_button(driver):

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

    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page.is_catalog_visible()
    menu_page.click_logout()

    dialog_page = DialogPage(driver)
    assert dialog_page.is_dialog_displayed()
    dialog_page.click_logout_button()

def test_logout_cancel_button(driver):

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

    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page.is_catalog_visible()
    menu_page.click_logout()

    dialog_page = DialogPage(driver)
    assert dialog_page.is_dialog_displayed()
    dialog_page.click_cancel_button()

    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page.is_catalog_visible()
    assert menu_page.is_logout_visible(), "Should still be logged in after cancel"

def test_simulate_real_login(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()

    login_page = LoginPage(driver)
    login_page.enter_username_keyboard("standard_user")
    login_page.enter_password_keyboard("10203040")
    login_page.click_login_button()

def test_screenshot(driver):

    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()

    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()
    products_page.screenshot(name="login_page")