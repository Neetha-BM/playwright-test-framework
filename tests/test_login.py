import pytest
import allure
from pages import LoginPage
from utils.config import VALID_USER, LOCKED_USER, PASSWORD


@allure.feature("Authentication")
class TestLogin:

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.login
    def test_valid_login(self, login_page: LoginPage):
        login_page.open()
        login_page.login(VALID_USER, PASSWORD)
        assert "inventory" in login_page.get_url()

    @allure.story("Locked User")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    def test_locked_user_cannot_login(self, login_page: LoginPage):
        login_page.open()
        login_page.login(LOCKED_USER, PASSWORD)
        login_page.expect_error_visible()
        login_page.expect_error_text("locked out")

    @allure.story("Empty Username")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login
    def test_empty_username(self, login_page: LoginPage):
        login_page.open()
        login_page.login("", PASSWORD)
        login_page.expect_error_visible()
        login_page.expect_error_text("Username is required")

    @allure.story("Empty Password")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login
    def test_empty_password(self, login_page: LoginPage):
        login_page.open()
        login_page.login(VALID_USER, "")
        login_page.expect_error_visible()
        login_page.expect_error_text("Password is required")

    @allure.story("Invalid Credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    def test_invalid_credentials(self, login_page: LoginPage):
        login_page.open()
        login_page.login("invalid_user", "wrong_password")
        login_page.expect_error_visible()
        login_page.expect_error_text("do not match")
