from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for Login Page"""

    # Locators
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "#submit"
    SUCCESS_MESSAGE = ".post-title"
    ERROR_MESSAGE = "#error"
    LOGOUT_BUTTON = "a:has-text('Log out')"

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://practicetestautomation.com/practice-test-login/"

    def open(self):
        """Open the login page"""
        self.navigate(self.url)

    def enter_username(self, username):
        """Enter username in the username field"""
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button"""
        self.click(self.SUBMIT_BUTTON)

    def login(self, username, password):
        """Perform login with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_login_successful(self):
        """Check if login was successful"""
        return self.is_visible(self.SUCCESS_MESSAGE) and self.is_visible(self.LOGOUT_BUTTON)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)
