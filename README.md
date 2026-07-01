# Playwright + Python Test Automation Framework

A production-grade UI test automation framework built with **Playwright**, **Python**, and **pytest**, following the **Page Object Model (POM)** design pattern.

## Architecture

```
playwright-test-framework/
├── pages/                    # Page Object classes
│   ├── base_page.py          # Base page with shared methods
│   ├── login_page.py         # Login page interactions
│   ├── inventory_page.py     # Product listing page
│   ├── cart_page.py           # Shopping cart page
│   └── checkout_page.py      # Checkout flow pages
├── tests/                    # Test suites
│   ├── conftest.py           # Fixtures & hooks (auto-screenshot on failure)
│   ├── test_login.py         # Authentication tests
│   ├── test_inventory.py     # Product browsing & sorting tests
│   ├── test_cart.py           # Cart management tests
│   ├── test_checkout.py      # End-to-end checkout tests
│   └── test_local_app.py     # Tests against bundled local demo app
├── utils/
│   └── config.py             # Environment configuration
├── local_app/
│   └── index.html            # Self-contained demo app for offline testing
├── .github/workflows/
│   └── tests.yml             # CI pipeline (Chromium, Firefox, WebKit)
├── pytest.ini                # pytest configuration & markers
├── requirements.txt          # Python dependencies
└── .env.example              # Environment variables template
```

## Key Features

- **Page Object Model** — Clean separation between test logic and page interactions
- **Cross-browser testing** — Chromium, Firefox, and WebKit via Playwright
- **Allure Reporting** — Rich HTML reports with screenshots on failure
- **CI/CD Ready** — GitHub Actions workflow with matrix strategy
- **Dual test targets** — Real public app (SauceDemo) + bundled local app
- **Custom pytest markers** — `@smoke`, `@regression`, `@login`, `@cart`, `@checkout`, `@local`

## Setup

```bash
# Clone and install
git clone <repo-url>
cd playwright-test-framework
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Install browsers
playwright install chromium

# Copy environment config
cp .env.example .env
```

## Running Tests

```bash
# Run all tests
pytest

# Run with Allure reporting
pytest --alluredir=allure-results
allure serve allure-results

# Run by marker
pytest -m smoke          # Quick sanity tests
pytest -m regression     # Full regression suite
pytest -m login          # Login tests only
pytest -m local          # Local app tests only

# Run specific browser
pytest --browser firefox
pytest --browser webkit

# Run headed (visible browser)
pytest --headed

# Parallel execution
pytest -n auto
```

## Test Coverage

| Feature       | Tests | Scenarios                                              |
|---------------|-------|--------------------------------------------------------|
| Login         | 5     | Valid login, locked user, empty fields, invalid creds  |
| Inventory     | 7     | Product display, sorting (4 options), add/remove cart  |
| Cart          | 4     | View items, remove items, continue shopping, checkout  |
| Checkout      | 7     | Complete flow, validation, cancel, back to products    |
| Local App     | 5     | Login, validation, logout (offline/self-contained)     |
| **Total**     | **28**|                                                        |

## Technologies

- **Python 3.12+**
- **Playwright** — Modern browser automation
- **pytest** — Test runner with fixtures and markers
- **Allure** — Test reporting
- **GitHub Actions** — CI/CD

## Author

Neetha B. — Senior QA Automation Engineer
