import pytest
import allure
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage
from utils.config import VALID_USER, PASSWORD, BASE_URL


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    # Maximize the browser window on launch for better visibility
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # Disable fixed viewport so the window fills the maximized screen
    return {**browser_context_args, "no_viewport": True}


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def authenticated_page(page):
    """Pre-login fixture: navigates to SauceDemo and logs in with standard_user."""
    login = LoginPage(page)
    login.open()
    login.login(VALID_USER, PASSWORD)
    page.wait_for_url("**/inventory.html")
    return page


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, page):
    """Capture a screenshot and attach to Allure report on test failure."""
    yield
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        allure.attach(
            page.screenshot(),
            name="failure-screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
