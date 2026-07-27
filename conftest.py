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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically take screenshot on test failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Create screenshot directory
            import os
            from datetime import datetime
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            filename = f"FAILED_{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshot_dir, filename)
            
            driver.get_screenshot_as_file(filepath)
            print(f"\nScreenshot saved on failure: {filepath}")