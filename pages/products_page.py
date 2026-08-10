from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from enum import Enum

class SortOption(Enum):
    SORT_ASCENDING_NAME = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameAscCL")
    SORT_DESCENDING_NAME = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameDesCL")
    SORT_ASCENDING_PRICE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceAscCL")
    SORT_DESCENDING_PRICE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceDesCL")


class Products(BasePage):

    PRODUCTS_TITLE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    MENU_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV")

    FIRST_PRODUCT_IMAGE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    FIRST_PRODUCT_NAME = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")

    SORT_ITEM_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/sortIV")
    SORT_MODAL = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup')
    
    cart_badge = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")
    cart_icon = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartRL")


    def wait_for_products_screen(self):
        self.find(*self.PRODUCTS_TITLE)

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT_IMAGE)

    def get_first_product_name(self):
        return self.get_text(*self.FIRST_PRODUCT_NAME)
    
    def click_menu_button(self):
        self.click(*self.MENU_BUTTON)

    def click_cart_button(self):
        self.click(*self.cart_icon)

    def click_sort_button(self):
        self.click(*self.SORT_ITEM_BUTTON)

    def get_cart_count(self):
        try:
            #print(f"Cart Badge text: {self.get_text(*self.cart_badge)}")    
            return self.get_text(*self.cart_badge)
        except:
            return 0

    def click_product_by_name(self, product_name):
        self.scroll_and_find_text(product_name)
        xpath = (
            f'//android.widget.TextView[@text="{product_name}"]'
            f'/preceding-sibling::android.widget.ImageView'
        )
        self.click(AppiumBy.XPATH, xpath)

    def verify_sort_modal(self):
        try:
            modal = self.find(*self.SORT_MODAL)
            return modal.is_displayed()
        except Exception:
            return False
