class BasePage:
    """Base class for all page objects"""

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        """Navigate to a given URL"""
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector):
        """Click an element"""
        self.page.click(selector)

    def fill(self, selector, text):
        """Fill text in an input field"""
        self.page.fill(selector, text)

    def get_text(self, selector):
        """Get text from an element"""
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector):
        """Check if an element is visible"""
        return self.page.locator(selector).is_visible()

    def get_content(self):
        """Get page content"""
        return self.page.content()
