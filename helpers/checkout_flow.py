from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.products_page import Products
from pages.product_detail_page import ProductDetailPage
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage

class CheckoutFlow:

    def __init__(self, driver):
        self.driver = driver

    def reach_checkout_title(self):
        products_page = Products(self.driver)
        menu_page = MenuPage(self.driver)
        login_page = LoginPage(self.driver)
        product_detail_page = ProductDetailPage(self.driver)
        cartPage = CartPage(self.driver)
        checkoutPage = CheckoutPage(self.driver)

        products_page.wait_for_products_screen()
        products_page.click_menu_button()
        menu_page.click_login()
        login_page.login("standard_user", "10203040")
        products_page.click_first_product()
        product_detail_page.click_add_to_cart()
        products_page.click_cart_button()
        cartPage.click_checkout_button()
        checkoutPage.is_checkout_title_displayed()