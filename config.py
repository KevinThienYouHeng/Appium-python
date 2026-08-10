# config.py
import os

class AppiumConfig:

    DEVICE_NAME = os.getenv("APPIUM_DEVICE", "emulator-5554")
    APK_PATH = os.getenv("APPIUM_APK", "mda-2.2.0-25.apk")

    LOCAL_APP_PACKAGE = "com.saucelabs.mydemoapp.android"
    LOCAL_APP_ACTIVITY = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    LOCAL_APP_WAIT_ACTIVITY = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"

    CI_APK_PATH = os.getenv("APPIUM_APK", "mda-2.2.0-25.apk")
    APPIUM_SERVER = os.getenv("APPIUM_SERVER", "http://localhost:4723")

    AUTO_GRANT_PERMISSIONS = True
    NO_RESET_LOCAL = True        # don't reinstall app every test (faster)
    NO_RESET_CI = False

    IMPLICIT_WAIT = 10

config = AppiumConfig()