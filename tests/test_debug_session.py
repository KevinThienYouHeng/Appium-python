from appium.webdriver.common.appiumby import AppiumBy

def test_driver_session_alive(driver):
    """Verify the session stays alive for 5 seconds."""
    import time
    print(f"Session created: {driver.session_id}")
    time.sleep(2)
    
    # Try a simple command
    print(f"Current package: {driver.current_package}")
    time.sleep(2)
    
    print("Session still alive!")
    assert True