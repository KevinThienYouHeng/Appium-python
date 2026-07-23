import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554 "      # <-- from: adb devices
    #options.device_name = "0005214BF000108 "
    options.app_package = "com.saucelabs.mydemoapp.android"
    options.app_activity = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    options.app_wait_activity = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"
    options.automation_name = "UiAutomator2"
    #options.no_reset = True                       # Keeps app state between sessions

    driver = webdriver.Remote("http://localhost:4723", options=options)
    
    yield driver
    
    driver.quit()