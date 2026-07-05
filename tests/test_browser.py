import pytest
import allure
from pathlib import Path
from playwright.sync_api import Page, Browser, expect

LOCAL_APP_PATH = Path(__file__).parent.parent / "local_app" / "index.html"
LOCAL_APP_URL = f"file:///{LOCAL_APP_PATH.resolve().as_posix()}"

PAUSE = 1500  # ms between steps so each action is clearly visible


def do_login_and_logout(page: Page):
    """Navigate to app, fill credentials, click login, verify welcome, then logout."""
    page.goto(LOCAL_APP_URL)
    page.wait_for_timeout(PAUSE)  # pause to see the login page load

    page.fill("[data-test='username']", "demo_user")
    page.wait_for_timeout(PAUSE)  # pause to see username typed

    page.fill("[data-test='password']", "demo_pass")
    page.wait_for_timeout(PAUSE)  # pause to see password typed

    page.click("[data-test='login-button']")
    page.wait_for_timeout(PAUSE)  # pause to see the welcome screen after redirect

    expect(page.locator("[data-test='welcome-message']")).to_be_visible()

    page.click("[data-test='logout-button']")
    page.wait_for_timeout(PAUSE)  # pause to see return to login screen


def show_viewport_label(page: Page, width: int, height: int):
    """Inject a visible label showing the current viewport size."""
    page.evaluate(f"""() => {{
        const el = document.createElement('div');
        el.style.cssText = `
            position: fixed; bottom: 20px; right: 20px;
            background: #333; color: #fff;
            padding: 10px 16px; font-size: 18px; font-weight: bold;
            border-radius: 6px; z-index: 9999; font-family: monospace;
        `;
        el.textContent = 'Viewport: {width} x {height}';
        document.body.appendChild(el);
    }}""")
    page.wait_for_timeout(PAUSE)  # pause so the label is clearly visible


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
        do_login_and_logout(page)
        # Read actual OS window size via CDP
        client = page.context.new_cdp_session(page)
        result = client.send("Browser.getWindowForTarget")
        size = result["bounds"]
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
        do_login_and_logout(page)
        show_viewport_label(page, 1280, 720)
        size = page.viewport_size
        context.close()
        assert size["width"] == 1280, f"Expected width 1280, got {size['width']}"
        assert size["height"] == 720, f"Expected height 720, got {size['height']}"

    @allure.story("Resize to Tablet 768x1024")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_tablet(self, browser: Browser):
        context = browser.new_context(viewport={"width": 768, "height": 1024})
        page = context.new_page()
        do_login_and_logout(page)
        show_viewport_label(page, 768, 1024)
        size = page.viewport_size
        context.close()
        assert size["width"] == 768, f"Expected width 768, got {size['width']}"
        assert size["height"] == 1024, f"Expected height 1024, got {size['height']}"

    @allure.story("Resize to Mobile 375x812")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.browser
    def test_resize_to_mobile(self, browser: Browser):
        context = browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()
        do_login_and_logout(page)
        show_viewport_label(page, 375, 812)
        size = page.viewport_size
        context.close()
        assert size["width"] == 375, f"Expected width 375, got {size['width']}"
        assert size["height"] == 812, f"Expected height 812, got {size['height']}"
