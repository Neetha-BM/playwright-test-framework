import pytest
import allure
from pathlib import Path
from playwright.sync_api import Page, Browser, expect

LOCAL_APP_PATH = Path(__file__).parent.parent / "local_app" / "index.html"
LOCAL_APP_URL = f"file:///{LOCAL_APP_PATH.resolve().as_posix()}"

PAUSE = 1500  # ms between steps so each action is clearly visible


def get_window_size(page: Page) -> dict:
    return page.evaluate(
        "() => ({ width: window.innerWidth, height: window.innerHeight })"
    )


def do_login(page: Page):
    """Navigate to local app, fill credentials, click login, and wait for welcome screen."""
    page.goto(LOCAL_APP_URL)
    page.wait_for_timeout(PAUSE)  # pause to see the login page load

    page.fill("[data-test='username']", "demo_user")
    page.wait_for_timeout(PAUSE)  # pause to see username typed

    page.fill("[data-test='password']", "demo_pass")
    page.wait_for_timeout(PAUSE)  # pause to see password typed

    page.click("[data-test='login-button']")
    page.wait_for_timeout(PAUSE)  # pause to see the welcome screen after login

    expect(page.locator("[data-test='welcome-message']")).to_be_visible()

    page.click("[data-test='logout-button']")
    page.wait_for_timeout(PAUSE)  # pause to see the return to login screen


@allure.feature("Browser Window")
class TestBrowserResize:

    @allure.story("Maximized on Launch")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    @pytest.mark.smoke
    def test_window_is_maximized_on_launch(self, page: Page):
        screen = page.evaluate(
            "() => ({ width: window.screen.availWidth, height: window.screen.availHeight })"
        )
        do_login(page)
        size = get_window_size(page)
        # Window should cover at least 90% of the available screen dimensions
        assert size["width"] >= screen["width"] * 0.9, (
            f"Expected width close to {screen['width']}, got {size['width']}"
        )
        assert size["height"] >= screen["height"] * 0.9, (
            f"Expected height close to {screen['height']}, got {size['height']}"
        )

    @allure.story("Resize to Desktop 1280x720")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_desktop(self, browser: Browser):
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()
        do_login(page)
        size = get_window_size(page)
        assert size["width"] == 1280, f"Expected width 1280, got {size['width']}"
        assert size["height"] == 720, f"Expected height 720, got {size['height']}"
        context.close()

    @allure.story("Resize to Tablet 768x1024")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_tablet(self, browser: Browser):
        context = browser.new_context(viewport={"width": 768, "height": 1024})
        page = context.new_page()
        do_login(page)
        size = get_window_size(page)
        assert size["width"] == 768, f"Expected width 768, got {size['width']}"
        assert size["height"] == 1024, f"Expected height 1024, got {size['height']}"
        context.close()

    @allure.story("Resize to Mobile 375x812")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_mobile(self, browser: Browser):
        context = browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()
        do_login(page)
        size = get_window_size(page)
        assert size["width"] == 375, f"Expected width 375, got {size['width']}"
        assert size["height"] == 812, f"Expected height 812, got {size['height']}"
        context.close()
