import pytest
import allure
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage
from utils.config import VALID_USER, PASSWORD


@allure.feature("Checkout")
class TestCheckout:

    @pytest.fixture
    def cart_with_item(self, authenticated_page):
        """Add an item to cart and navigate to checkout."""
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart_by_name("sauce-labs-backpack")
        inventory.go_to_cart()
        cart = CartPage(authenticated_page)
        cart.proceed_to_checkout()
        return authenticated_page

    @allure.story("Complete Checkout")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_complete_checkout_flow(self, cart_with_item):
        checkout = CheckoutPage(cart_with_item)
        checkout.fill_shipping_info("Jane", "Doe", "M5V 2T6")
        checkout.click_continue()
        assert "checkout-step-two" in checkout.get_url()

        total = checkout.get_total()
        assert "$" in total

        checkout.click_finish()
        checkout.expect_order_complete()

    @allure.story("Checkout Missing First Name")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.checkout
    def test_checkout_requires_first_name(self, cart_with_item):
        checkout = CheckoutPage(cart_with_item)
        checkout.fill_shipping_info("", "Doe", "M5V 2T6")
        checkout.click_continue()
        checkout.expect_error_visible()

    @allure.story("Checkout Missing Last Name")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.checkout
    def test_checkout_requires_last_name(self, cart_with_item):
        checkout = CheckoutPage(cart_with_item)
        checkout.fill_shipping_info("Jane", "", "M5V 2T6")
        checkout.click_continue()
        checkout.expect_error_visible()

    @allure.story("Checkout Missing Postal Code")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.checkout
    def test_checkout_requires_postal_code(self, cart_with_item):
        checkout = CheckoutPage(cart_with_item)
        checkout.fill_shipping_info("Jane", "Doe", "")
        checkout.click_continue()
        checkout.expect_error_visible()

    @allure.story("Cancel Checkout")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.checkout
    def test_cancel_checkout_returns_to_cart(self, cart_with_item):
        checkout = CheckoutPage(cart_with_item)
        checkout.click_cancel()
        assert "cart" in checkout.get_url()

    @allure.story("Back to Products After Order")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.checkout
    def test_back_home_after_complete_order(self, cart_with_item):
        checkout = CheckoutPage(cart_with_item)
        checkout.fill_shipping_info("Jane", "Doe", "M5V 2T6")
        checkout.click_continue()
        checkout.click_finish()
        checkout.go_back_home()
        assert "inventory" in checkout.get_url()
