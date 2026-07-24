from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class MenuPage(BasePage):

    catalog_item = (AppiumBy.XPATH, "//*[@text='Catalog']")
    about_item = (AppiumBy.XPATH, "//*[@text='About']")
    login_item = (AppiumBy.XPATH, "//*[@text='Log In']")
    webview_item = (AppiumBy.XPATH, "//*[@text='WebView']")
    code_scanner_item = (AppiumBy.XPATH, "//*[@text='QR Code Scanner']")
    location_item = (AppiumBy.XPATH, "//*[@text='Geo Location']")
    drawing_item = (AppiumBy.XPATH, "//*[@text='Drawing']")
    reset_app_item = (AppiumBy.XPATH, "//*[@text='Reset App State']")
    fingerprint_item = (AppiumBy.XPATH, "//*[@text='FingerPrint']")
    virtual_USB_item = (AppiumBy.XPATH, "//*[@text='Virtual USB']")
    logout_item = (AppiumBy.XPATH, "//*[@text='Log Out']")

    def is_catalog_visible(self):
        return self.is_displayed(*self.catalog_item)

    def click_catalog(self):
        self.click(*self.catalog_item)

    def click_about(self):
        self.click(*self.about_item)

    def click_login(self):
        self.click(*self.login_item)

    def click_logout(self):
        self.click(*self.logout_item)

    def is_login_visible(self):
        return self.is_displayed(*self.login_item)
    
    def is_logout_visible(self):
        return self.is_displayed(*self.logout_item)