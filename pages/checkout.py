from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    checkout_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/checkoutTitleTV")
    full_name_input = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
    full_name_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Full Name*"]')
    address_line1 = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
    address_line2 = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address2ET")
    city_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")
    zip_code = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")
    country_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")
    state_item = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/stateET")
    payment_button = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
    shipping_fields = [
        full_name_input,
        address_line1,
        address_line2,
        city_item,
        zip_code,
        country_item,
        state_item
    ]

    #errorObjects
    full_name_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameErrorTV")
    address_line1_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ErrorTV")
    city_item_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityErrorTV")
    zip_code_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipErrorTV")
    country_item_error = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryErrorTV")
    error_icon = (AppiumBy.ACCESSIBILITY_ID, "Indicates error")

    #parentObjects
    full_name_parent = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameRL")
    address_line1_parent = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1RL")
    city_item_parent = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityRL")
    zip_code_parent = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipRL")
    country_item_parent = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryRL")
    state_item_parent = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/stateRL") 

    def is_checkout_title_displayed(self):     
        return self.is_displayed(*self.checkout_title)

    def get_checkout_title(self):
        return self.get_text(*self.checkout_title)

    #This is call helper function to reach checkout title from products page, login page, product detail page, cart page
    

    def verify_checkout_page(self):
        self.double_click(*self.full_name_input)
        self.double_click(*self.address_line1)
        self.double_click(*self.address_line2)
        self.double_click(*self.city_item)
        self.double_click(*self.zip_code)
        self.double_click(*self.state_item)
        self.double_click(*self.country_item)

    def enter_full_name(self, name):
        self.find(*self.full_name_input).send_keys(name)

    def verify_placeholder_full_name(self):
        placeholder = self.find(*self.full_name_label).get_attribute("hint")
        return placeholder == "Full Name"

    def enter_address_line1(self, address1):
        self.find(*self.address_line1).send_keys(address1)

    def enter_city(self, city):
        self.find(*self.city_item).send_keys(city)

    def enter_zip_code(self, zip_code):
        self.find(*self.zip_code).send_keys(zip_code)

    def enter_state(self, state):
        self.find(*self.state_item).send_keys(state)

    def enter_country(self, country):
        self.find(*self.country_item).send_keys(country)

    def click_payment_button(self):
        self.click(*self.payment_button)

    def verify_full_name_field(self):

        errors = []

        try:
            label = self.find(*self.full_name_label)
            if not label.is_displayed():
                errors.append("Full Name field is not displayed.")
        except Exception as e:
            errors.append(f"Error while verifying Full Name field: {str(e)}")

        try:
            field = self.find(*self.full_name_input)
            if not field.is_enabled():
                errors.append("Full Name field is not enabled.")
        except Exception as e:
            errors.append(f"Error while verifying Full Name field: {str(e)}")

        if not errors:
            actual_value = field.get_attribute("text") or ""
            expected_value = "Rebecca Winter"
            if actual_value != expected_value:
                errors.append(f"Expected Full Name field value to be '{expected_value}', but found '{actual_value}'.")

        if errors:
            raise AssertionError("\n".join(errors))

        return True

    # def verify_full_name_error_message(self):
    #     name_error = self.get_text(*self.full_name_error)
    #     print(f"Full Name Error Message: {name_error}")

    #     actual_value = self.find(*self.full_name_error).get_attribute("text")
    #     expected_value = "Full Name is required"
    #     if actual_value != expected_value:
    #         raise AssertionError(f"Expected Full Name error message to be '{expected_value}', but found '{actual_value}'.")
        
    #     return self.is_displayed(*self.full_name_error) 

    def verify_full_name_error_message(self, expected_message: str = "Please provide your full name."):
        error_element = self.find(*self.full_name_error)

        assert error_element.is_displayed(), "Full Name error message is not displayed."

        actual_message = error_element.text
        assert actual_message == expected_message, (
            f"Full Name error message mismatch.\n"
            f"Expected: '{expected_message}'\n"
            f"Actual:   '{actual_message}'"
        )

        return self

    #this functions is reusable for all error messages, just pass the error locator and expected message
    def verify_field_error(self, error_locator, expected_message: str):
   
        error_element = self.find(*error_locator)
        assert error_element.is_displayed(), "Error element is not displayed"
        
        actual = error_element.text
        assert actual == expected_message, (
            f"Error message mismatch.\n"
            f"Expected: '{expected_message}'\n"
            f"Actual:   '{actual}'"
        )
        
        return self

    def verify_field_error_icon(self, parent_locator, field_name: str = "Field"):
        parent = self.find(*parent_locator)
        error_icon = parent.find_element(*self.error_icon)
        assert error_icon.is_displayed(), f"{field_name} error icon is not displayed"
        return True

    def reach_checkout_page_two(self):
        self.enter_full_name("John Doe")
        self.enter_address_line1("123 Main St")
        self.enter_city("Anytown")
        self.enter_zip_code("12345")
        self.enter_state("CA")
        self.enter_country("USA")
        self.click_payment_button()