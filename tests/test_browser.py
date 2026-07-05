import pytest
import allure
from playwright.sync_api import Page, Browser


def get_window_size(page: Page) -> dict:
    return page.evaluate(
        "() => ({ width: window.innerWidth, height: window.innerHeight })"
    )


@allure.feature("Browser Window")
class TestBrowserResize:

    @allure.story("Maximized on Launch")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    @pytest.mark.smoke
    def test_window_is_maximized_on_launch(self, page: Page):
        page.goto("about:blank")
        page.wait_for_timeout(1000)
        screen = page.evaluate(
            "() => ({ width: window.screen.availWidth, height: window.screen.availHeight })"
        )
        size = get_window_size(page)
        # Window should cover at least 90% of the available screen dimensions
        assert size["width"] >= screen["width"] * 0.9, (
            f"Expected width close to {screen['width']}, got {size['width']}"
        )
        assert size["height"] >= screen["height"] * 0.9, (
            f"Expected height close to {screen['height']}, got {size['height']}"
        )

    @allure.story("Resize to Desktop")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_desktop(self, browser: Browser):
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()
        page.goto("about:blank")
        # Brief pause so the resized window is visible before asserting
        page.wait_for_timeout(1000)
        size = get_window_size(page)
        assert size["width"] == 1280, f"Expected width 1280, got {size['width']}"
        assert size["height"] == 720, f"Expected height 720, got {size['height']}"
        context.close()

    @allure.story("Resize to Tablet")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_tablet(self, browser: Browser):
        context = browser.new_context(viewport={"width": 768, "height": 1024})
        page = context.new_page()
        page.goto("about:blank")
        # Brief pause so the resized window is visible before asserting
        page.wait_for_timeout(1000)
        size = get_window_size(page)
        assert size["width"] == 768, f"Expected width 768, got {size['width']}"
        assert size["height"] == 1024, f"Expected height 1024, got {size['height']}"
        context.close()

    @allure.story("Resize to Mobile")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_mobile(self, browser: Browser):
        context = browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()
        page.goto("about:blank")
        # Brief pause so the resized window is visible before asserting
        page.wait_for_timeout(1000)
        size = get_window_size(page)
        assert size["width"] == 375, f"Expected width 375, got {size['width']}"
        assert size["height"] == 812, f"Expected height 812, got {size['height']}"
        context.close()
