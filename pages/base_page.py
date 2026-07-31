import os
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def find(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        self.find(by, value).click()

    def get_text(self, by, value):
        return self.find(by, value).text
    
    def is_displayed(self, by, value):
        try:
            return self.find(by, value).is_displayed()
        except:
            return False

    def screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)
        self.driver.get_screenshot_as_file(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath

    def scroll_to_text(self, text):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))')