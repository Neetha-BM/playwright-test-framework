import pytest
import allure
from pages import InventoryPage, CartPage


@allure.feature("Shopping Cart")
class TestCart:

    @allure.story("View Cart Items")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.cart
    def test_added_items_appear_in_cart(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart_by_name("sauce-labs-backpack")
        inventory.add_item_to_cart_by_name("sauce-labs-bike-light")
        inventory.go_to_cart()

        cart = CartPage(authenticated_page)
        assert cart.get_cart_item_count() == 2
        names = cart.get_item_names()
        assert "Sauce Labs Backpack" in names
        assert "Sauce Labs Bike Light" in names

    @allure.story("Remove Item from Cart Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.cart
    def test_remove_item_from_cart(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart_by_name("sauce-labs-backpack")
        inventory.go_to_cart()

        cart = CartPage(authenticated_page)
        cart.remove_item_by_name("sauce-labs-backpack")
        assert cart.get_cart_item_count() == 0

    @allure.story("Continue Shopping")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.cart
    def test_continue_shopping_returns_to_inventory(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.go_to_cart()

        cart = CartPage(authenticated_page)
        cart.continue_shopping()
        assert "inventory" in cart.get_url()

    @allure.story("Empty Cart Checkout")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.cart
    def test_can_proceed_to_checkout_with_empty_cart(self, authenticated_page):
        inventory = InventoryPage(authenticated_page)
        inventory.go_to_cart()

        cart = CartPage(authenticated_page)
        cart.proceed_to_checkout()
        assert "checkout-step-one" in cart.get_url()
