
# tests/test_sample.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_demo_app_opens(driver):
    # Just wait for ANY element to appear - proves the app loaded
    wait = WebDriverWait(driver, 10)
    any_element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//*"))
    )
    
    # Get current app package to confirm we're in the right app
    current_package = driver.current_package
    assert current_package == "com.saucelabs.mydemoapp.android"

def test_products_title_visible(driver):
    """Wait for the Products screen and verify the title text."""
    wait = WebDriverWait(driver, 10)
    
    logo = driver.find_element(
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/mTvTitle"
    )

    # Wait for the "Products" title element
    products_title = wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID, 
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )
    
    # Read the text and assert it
    assert logo.is_displayed()
    assert products_title.text == "Products"

def test_first_product_name(driver):
    """Verify the first product in the list is 'Sauce Labs Backpack'."""
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID, 
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )
    # titleTV appears for every product. find_element returns the FIRST one.
    first_product_name = driver.find_element(
        AppiumBy.ID, 
        "com.saucelabs.mydemoapp.android:id/titleTV"
    )
    
    assert first_product_name.text == "Sauce Labs Backpack"

def test_click_first_product(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"))
    )
    
    first_product = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    first_product.click()
    
    product_title = wait.until(
        EC.visibility_of_element_located((AppiumBy.XPATH, "//*[@text='Sauce Labs Backpack']"))
    )
    
    assert product_title.is_displayed()

def test_product_detail_price(driver):
    """Click first product and verify the price on detail screen."""
    wait = WebDriverWait(driver, 10)
    
    # On Products screen: click first product
    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID, 
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )
    driver.find_element(
        AppiumBy.ID, 
        "com.saucelabs.mydemoapp.android:id/productIV"
    ).click()
    
    # On Detail screen: find the price element
    # Use XPath because we know the text. You can also find the ID in Appium Inspector.
    price = wait.until(
        EC.visibility_of_element_located((
            AppiumBy.XPATH, 
            "//*[@text='$ 29.99']"
        ))
    )
    
    assert price.text == "$ 29.99"


def test_back_button_return_to_products(driver):

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )

    driver.find_element(
        AppiumBy.ID, 
        "com.saucelabs.mydemoapp.android:id/productIV"
    ).click()

    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.XPATH,
            "//*[@text='$ 29.99']"
        ))
    )

    driver.back()

    products_title = wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID, 
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )

    assert products_title.text == "Products"
    assert products_title.is_displayed()

def test_menu_button(driver):

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )

    driver.find_element(
        AppiumBy.ID, 
        "com.saucelabs.mydemoapp.android:id/menuIV"
    ).click()

    menu_item = wait.until(
        EC.visibility_of_element_located((
            AppiumBy.XPATH,
            "//*[@text='Catalog']"
        ))
    )

    assert menu_item.is_displayed()

def test_scroll_to_find_bolt_tshirt(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Sauce Labs Bolt T-Shirt"))'
    )

    bolt_tshirt = wait.until(
        EC.visibility_of_element_located((
            AppiumBy.XPATH,
            "//*[@text='Sauce Labs Bolt T-Shirt']"
        ))
    )

    print(f"Bolt T-Shirt: {bolt_tshirt.text}")
    assert bolt_tshirt.is_displayed()

def test_scroll_bottom(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)')
    
    last_product = driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/titleTV'])[last()]")

    assert last_product.is_displayed()
    print(f"Last product: {last_product.text}")

def test_scroll_bottom_Top(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/productTV"
        ))
    )

    first_product = driver.find_element(
        AppiumBy.ID, 
        "com.saucelabs.mydemoapp.android:id/titleTV"
    )
    first_product_name = first_product.text
    print(f"First product before scroll: {first_product_name}")

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)')
    
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)')
    
    first_product_after = wait.until(
        EC.visibility_of_element_located((
            AppiumBy.ID, 
            "com.saucelabs.mydemoapp.android:id/titleTV"
        ))
    )
    first_product_after_name = first_product_after.text
    print(f"First product after scroll: {first_product_after_name}")

    assert first_product_after_name == first_product_name
    assert first_product_after.is_displayed()