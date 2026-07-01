from playwright.sync_api import Page, expect
from .base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"
    INVENTORY_LIST = "[data-test='inventory-list']"
    INVENTORY_ITEM = "[data-test='inventory-item']"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    SHOPPING_CART_BADGE = "[data-test='shopping-cart-badge']"
    SHOPPING_CART_LINK = "[data-test='shopping-cart-link']"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_inventory_items(self):
        return self.page.locator(self.INVENTORY_ITEM).all()

    def get_item_count(self) -> int:
        return len(self.get_inventory_items())

    def add_item_to_cart_by_index(self, index: int):
        items = self.get_inventory_items()
        items[index].locator("button").click()
        return self

    def add_item_to_cart_by_name(self, name: str):
        item_id = name.lower().replace(" ", "-")
        self.page.click(f"[data-test='add-to-cart-{item_id}']")
        return self

    def remove_item_from_cart_by_name(self, name: str):
        item_id = name.lower().replace(" ", "-")
        self.page.click(f"[data-test='remove-{item_id}']")
        return self

    def get_cart_badge_count(self) -> int:
        if self.page.is_visible(self.SHOPPING_CART_BADGE):
            return int(self.page.text_content(self.SHOPPING_CART_BADGE))
        return 0

    def go_to_cart(self):
        self.page.click(self.SHOPPING_CART_LINK)
        return self

    def sort_by(self, value: str):
        self.page.select_option(self.SORT_DROPDOWN, value)
        return self

    def get_item_names(self) -> list[str]:
        return self.page.locator("[data-test='inventory-item-name']").all_text_contents()

    def get_item_prices(self) -> list[float]:
        prices = self.page.locator("[data-test='inventory-item-price']").all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def logout(self):
        self.page.click(self.BURGER_MENU)
        self.page.click(self.LOGOUT_LINK)
        return self
