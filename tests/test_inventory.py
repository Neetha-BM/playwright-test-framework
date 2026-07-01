import pytest
import allure
from pages import InventoryPage


@allure.feature("Product Inventory")
class TestInventory:

    @allure.story("Display Products")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_inventory_displays_six_products(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        assert inventory.get_item_count() == 6

    @allure.story("Sort Products by Name A-Z")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_sort_by_name_ascending(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("az")
        names = inventory.get_item_names()
        assert names == sorted(names)

    @allure.story("Sort Products by Name Z-A")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_sort_by_name_descending(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("za")
        names = inventory.get_item_names()
        assert names == sorted(names, reverse=True)

    @allure.story("Sort Products by Price Low to High")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_sort_by_price_low_to_high(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("lohi")
        prices = inventory.get_item_prices()
        assert prices == sorted(prices)

    @allure.story("Sort Products by Price High to Low")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_sort_by_price_high_to_low(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("hilo")
        prices = inventory.get_item_prices()
        assert prices == sorted(prices, reverse=True)

    @allure.story("Add Item to Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.cart
    def test_add_item_updates_cart_badge(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart_by_name("sauce-labs-backpack")
        assert inventory.get_cart_badge_count() == 1

    @allure.story("Remove Item from Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.cart
    def test_remove_item_updates_cart_badge(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart_by_name("sauce-labs-backpack")
        assert inventory.get_cart_badge_count() == 1
        inventory.remove_item_from_cart_by_name("sauce-labs-backpack")
        assert inventory.get_cart_badge_count() == 0
