from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

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