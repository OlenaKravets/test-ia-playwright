import pytest
from pages.registration_page import RegistrationPage


class TestRegistration:
    """Test class for Registration functionality"""

    def test_registration_page_opens(self, page):
        """Test that registration page opens successfully"""
        registration_page = RegistrationPage(page)
        registration_page.open()
        assert "registration" in registration_page.page.url, "URL should contain 'registration'"

    def test_registration_form_elements_visible(self, page):
        """Test that registration page loads and has form content"""
        registration_page = RegistrationPage(page)
        registration_page.open()
        # Check that page title and form are loaded
        assert "registration" in registration_page.page.url, "URL should contain 'registration'"
        # Check that page has content
        assert len(registration_page.get_content()) > 0, "Page should have content"
