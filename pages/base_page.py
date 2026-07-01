from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        self.page.goto(path)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def take_screenshot(self, name: str) -> bytes:
        return self.page.screenshot(path=f"reports/{name}.png")

    def wait_for_element(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
