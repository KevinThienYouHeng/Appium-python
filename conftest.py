import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.ai_helper import ask_ai_to_analyze_failure
import os
from datetime import datetime
from config import config
from pages.products_page import Products
from pages.menu_page import MenuPage
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    if os.getenv("CI"):
        # ========== CI MODE (GitHub Actions) ==========
        options.device_name = "Android Emulator"
        # Appium will install this APK automatically before launching
        options.app = config.CI_APK_PATH
        # Auto-grant permissions so login/location popups don't block tests
        options.auto_grant_permissions = True
        
    else:
        # ========== LOCAL MODE ==========
        options.device_name = config.DEVICE_NAME  # <-- from: adb devices
        #options.device_name = "0005214BF000108 "
        options.app_package = config.LOCAL_APP_PACKAGE
        options.app_activity = config.LOCAL_APP_ACTIVITY
        options.app_wait_activity = config.LOCAL_APP_WAIT_ACTIVITY
    
    #options.no_reset = True                       # Keeps app state between sessions
    driver = webdriver.Remote(config.APPIUM_SERVER, options=options)
    
    try:
        # This forces Appium to confirm the session is real
        session_id = driver.session_id
        current_pkg = driver.current_package
        print(f"\n[SESSION] Created: {session_id} | Package: {current_pkg}")
    except Exception as e:
        driver.quit()
        raise RuntimeError(f"Driver session died immediately after creation: {e}")
    
    yield driver
    
    # Safe quit
    try:
        driver.quit()
    except Exception:
        pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Screenshot on test failure. No AI/RAG."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        
        if driver:
            try:
                screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"FAILED_{item.name}_{timestamp}.png"
                filepath = os.path.join(screenshot_dir, filename)
                
                driver.get_screenshot_as_file(filepath)
                print(f"\n[SCREENSHOT] {filepath}")
            except Exception as e:
                print(f"\n[SCREENSHOT] Skipped: {e}")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Automatically take screenshot on test failure."""
#     outcome = yield
#     rep = outcome.get_result()
    
#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("driver")
#         if driver:
#             # Create screenshot directory
#             import os
#             from datetime import datetime
#             screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
#             os.makedirs(screenshot_dir, exist_ok=True)
            
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             test_name = item.name
#             filename = f"FAILED_{test_name}_{timestamp}.png"
#             filepath = os.path.join(screenshot_dir, filename)
            
#             driver.get_screenshot_as_file(filepath)
#             print(f"\nScreenshot saved on failure: {filepath}")

#         error_text = str(rep.longrepr)
#         try:
#             ai_analysis = ask_ai_to_analyze_failure(error_text)
#             print(f"\n[AI ANALYSIS]\n{ai_analysis}")
#         except Exception as e:
#             # Don't let AI failure break the test report
#             print(f"\n[AI ANALYSIS] Skipped — {e}")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
    
#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("driver")
        
#         # --- Screenshot with protection ---
#         if driver:
#             try:
#                 import os
#                 from datetime import datetime
                
#                 screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
#                 os.makedirs(screenshot_dir, exist_ok=True)
                
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 filename = f"FAILED_{item.name}_{timestamp}.png"
#                 filepath = os.path.join(screenshot_dir, filename)
                
#                 driver.get_screenshot_as_file(filepath)
#                 print(f"\n[SCREENSHOT] {filepath}")
                
#             except Exception as e:
#                 print(f"\n[SCREENSHOT] Failed: {e}")
        
#         # --- AI analysis with protection ---
#         try:
#             error_text = str(rep.longrepr)[:2000]
#             from utils.ai_helper import ask_ai_to_analyze_failure
#             ai_analysis = ask_ai_to_analyze_failure(error_text)
#             print(f"\n[AI ANALYSIS]\n{ai_analysis}")
#         except Exception as e:
#             print(f"\n[AI ANALYSIS] Skipped: {e}")

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
    
#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("driver")
        
#         # Screenshot with protection
#         if driver:
#             try:
#                 screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
#                 os.makedirs(screenshot_dir, exist_ok=True)
                
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 filename = f"FAILED_{item.name}_{timestamp}.png"
#                 filepath = os.path.join(screenshot_dir, filename)
                
#                 driver.get_screenshot_as_file(filepath)
#                 print(f"\n[SCREENSHOT] {filepath}")
#             except Exception as e:
#                 print(f"\n[SCREENSHOT] Skipped: {e}")
        
#         # AI analysis — DISABLE RAG for now, use simple error text only
#         try:
#             error_text = str(rep.longrepr)[:1500]
#             print(f"\n[ERROR LOG]\n{error_text}")
#             # Skip RAG until Windows/Chroma issue is fixed
#         except Exception as e:
#             print(f"\n[AI] Skipped: {e}")

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

@pytest.fixture
def login_page(driver):
    products_page = Products(driver)
    products_page.wait_for_products_screen()
    products_page.click_menu_button()
    menu_page = MenuPage(driver)
    menu_page.is_catalog_visible()
    menu_page.click_login()
    return LoginPage(driver)