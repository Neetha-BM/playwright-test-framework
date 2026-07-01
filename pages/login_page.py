from playwright.sync_api import Page, expect
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(self.URL)
        return self

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.page.text_content(self.ERROR_MESSAGE)

    def expect_error_visible(self):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()

    def expect_error_text(self, text: str):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(text)
