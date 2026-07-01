from playwright.sync_api import Page, expect
from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    CANCEL_BUTTON = "[data-test='cancel']"
    FINISH_BUTTON = "[data-test='finish']"
    ERROR_MESSAGE = "[data-test='error']"
    SUMMARY_TOTAL = "[data-test='total-label']"
    COMPLETE_HEADER = "[data-test='complete-header']"
    BACK_HOME_BUTTON = "[data-test='back-to-products']"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def click_continue(self):
        self.page.click(self.CONTINUE_BUTTON)
        return self

    def click_finish(self):
        self.page.click(self.FINISH_BUTTON)
        return self

    def click_cancel(self):
        self.page.click(self.CANCEL_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.page.text_content(self.ERROR_MESSAGE)

    def expect_error_visible(self):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()

    def get_total(self) -> str:
        return self.page.text_content(self.SUMMARY_TOTAL)

    def get_complete_header(self) -> str:
        return self.page.text_content(self.COMPLETE_HEADER)

    def expect_order_complete(self):
        expect(self.page.locator(self.COMPLETE_HEADER)).to_have_text(
            "Thank you for your order!"
        )

    def go_back_home(self):
        self.page.click(self.BACK_HOME_BUTTON)
        return self
