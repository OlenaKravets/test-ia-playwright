import pytest
from pages.login_page import LoginPage

# Test data
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"
INVALID_PASSWORD = "wrong_password"


class TestLogin:
    """Test class for Login functionality"""

    def test_successful_login(self, page):
        """Test successful login with valid credentials"""
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        assert login_page.is_login_successful(), "Login should be successful"

    def test_login_with_wrong_password(self, page):
        """Test login with invalid password"""
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)
        assert login_page.is_error_displayed(), "Error message should be displayed"
        assert "invalid" in login_page.get_error_message().lower(), "Error message should contain 'invalid'"
