from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Page Object for Registration Page"""

    # Locators
    EMAIL_INPUT = "#email"
    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    PASSWORD_INPUT = "#password"
    CONFIRM_PASSWORD_INPUT = "#confirm_password"
    SUBMIT_BUTTON = "#submit"
    SUCCESS_MESSAGE = ".post-title"
    ERROR_MESSAGE = ".validation-error"

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://practicetestautomation.com/practice-test-registration/"

    def open(self):
        """Open the registration page"""
        self.navigate(self.url)

    def enter_email(self, email):
        """Enter email in the email field"""
        self.fill(self.EMAIL_INPUT, email)

    def enter_first_name(self, first_name):
        """Enter first name in the first name field"""
        self.fill(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        """Enter last name in the last name field"""
        self.fill(self.LAST_NAME_INPUT, last_name)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.fill(self.PASSWORD_INPUT, password)

    def enter_confirm_password(self, confirm_password):
        """Enter confirm password in the confirm password field"""
        self.fill(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    def click_register_button(self):
        """Click the register button"""
        self.click(self.SUBMIT_BUTTON)

    def register(self, email, first_name, last_name, password, confirm_password):
        """Perform registration with provided data"""
        self.enter_email(email)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_register_button()

    def is_registration_successful(self):
        """Check if registration was successful"""
        return self.is_visible(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)
