import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    """Fixture to initialize and teardown browser"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Fixture to create a new page for each test"""
    page = browser.new_page()
    yield page
    page.close()
