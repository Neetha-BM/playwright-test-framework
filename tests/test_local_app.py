import pytest
import allure
from pathlib import Path
from playwright.sync_api import Page, expect


LOCAL_APP_PATH = Path(__file__).parent.parent / "local_app" / "index.html"
LOCAL_APP_URL = f"file:///{LOCAL_APP_PATH.resolve().as_posix()}"


@allure.feature("Local Demo App")
class TestLocalApp:

    @pytest.fixture(autouse=True)
    def open_local_app(self, page: Page):
        page.goto(LOCAL_APP_URL)

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.local
    def test_successful_login(self, page: Page):
        page.fill("[data-test='username']", "demo_user")
        page.fill("[data-test='password']", "demo_pass")
        page.click("[data-test='login-button']")
        expect(page.locator("[data-test='welcome-message']")).to_be_visible()

    @allure.story("Empty Username")
    @pytest.mark.local
    def test_empty_username_shows_error(self, page: Page):
        page.fill("[data-test='password']", "demo_pass")
        page.click("[data-test='login-button']")
        expect(page.locator("[data-test='error']")).to_have_text("Username is required")

    @allure.story("Empty Password")
    @pytest.mark.local
    def test_empty_password_shows_error(self, page: Page):
        page.fill("[data-test='username']", "demo_user")
        page.click("[data-test='login-button']")
        expect(page.locator("[data-test='error']")).to_have_text("Password is required")

    @allure.story("Invalid Credentials")
    @pytest.mark.local
    def test_invalid_credentials_shows_error(self, page: Page):
        page.fill("[data-test='username']", "wrong")
        page.fill("[data-test='password']", "wrong")
        page.click("[data-test='login-button']")
        expect(page.locator("[data-test='error']")).to_have_text("Invalid username or password")

    @allure.story("Logout")
    @pytest.mark.local
    def test_logout_returns_to_login(self, page: Page):
        page.fill("[data-test='username']", "demo_user")
        page.fill("[data-test='password']", "demo_pass")
        page.click("[data-test='login-button']")
        page.click("[data-test='logout-button']")
        expect(page.locator("[data-test='login-button']")).to_be_visible()
