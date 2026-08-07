import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.ai_helper import ask_ai_to_analyze_failure
import os

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    if os.getenv("CI"):
        # ========== CI MODE (GitHub Actions) ==========
        options.device_name = "Android Emulator"
        # Appium will install this APK automatically before launching
        options.app = "mda-2.2.0-25.apk"
        # Auto-grant permissions so login/location popups don't block tests
        options.auto_grant_permissions = True
        
    else:
        # ========== LOCAL MODE ==========
        options.device_name = "emulator-5554"  # <-- from: adb devices
        #options.device_name = "0005214BF000108 "
        options.app_package = "com.saucelabs.mydemoapp.android"
        options.app_activity = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        options.app_wait_activity = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"
    
    
    
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

        error_text = str(rep.longrepr)
        try:
            ai_analysis = ask_ai_to_analyze_failure(error_text)
            print(f"\n[AI ANALYSIS]\n{ai_analysis}")
        except Exception as e:
            # Don't let AI failure break the test report
            print(f"\n[AI ANALYSIS] Skipped — {e}")

def get_android_capabilities():
    """
    Returns capabilities. In CI, the emulator is already running on localhost:4723.
    Locally, you run Appium server yourself.
    """
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"
    
    # Path to your APK. In CI we will download it to this path.
    options.app = "mda-2.2.0-25.apk"
    
    # Auto-grant permissions so the login flow isn't blocked
    options.auto_grant_permissions = True
    
    # Don't reset app data between tests in the same session
    # (We use fullReset=False in CI so login state persists briefly)
    options.no_reset = False
    
    return options