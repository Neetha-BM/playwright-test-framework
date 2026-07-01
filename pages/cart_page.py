from playwright.sync_api import Page, expect
from .base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"
    CART_ITEM = "[data-test='inventory-item']"
    CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    REMOVE_BUTTON = "button[data-test^='remove-']"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_cart_items(self):
        return self.page.locator(self.CART_ITEM).all()

    def get_cart_item_count(self) -> int:
        return len(self.get_cart_items())

    def get_item_names(self) -> list[str]:
        return self.page.locator("[data-test='inventory-item-name']").all_text_contents()

    def remove_item_by_name(self, name: str):
        item_id = name.lower().replace(" ", "-")
        self.page.click(f"[data-test='remove-{item_id}']")
        return self

    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING_BUTTON)
        return self

    def proceed_to_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)
        return self
