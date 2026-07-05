# Playwright + TypeScript Test Automation Framework

A production-grade UI test automation framework built with **Playwright**, **TypeScript**, and **Node.js**, following the **Page Object Model (POM)** design pattern.

## Architecture

```
playwright-test-framework/
├── src/
│   ├── pages/                    # Page Object classes (TypeScript)
│   │   ├── BasePage.ts           # Base class with shared methods and demo pauses
│   │   ├── LoginPage.ts          # Login page interactions
│   │   ├── InventoryPage.ts      # Product listing page
│   │   ├── CartPage.ts           # Shopping cart page
│   │   └── CheckoutPage.ts       # Checkout flow pages
│   ├── tests/                    # Test specs
│   │   ├── login.spec.ts         # Authentication tests
│   │   ├── inventory.spec.ts     # Product browsing & sorting tests
│   │   ├── cart.spec.ts          # Cart management tests
│   │   ├── checkout.spec.ts      # End-to-end checkout tests
│   │   └── browser.spec.ts       # Viewport & browser resize tests
│   └── utils/
│       └── config.ts             # Environment configuration
├── .github/workflows/
│   └── ts-tests.yml              # CI pipeline (Chromium)
├── playwright.config.ts          # Playwright configuration
├── package.json                  # Node dependencies
└── tsconfig.json                 # TypeScript configuration
```

## Key Features

- **Page Object Model** — Clean separation between test logic and page interactions
- **TypeScript** — Full type safety across pages, fixtures, and test utilities
- **Cross-browser testing** — Chromium, Firefox, and WebKit via Playwright
- **HTML Reporting** — Rich built-in Playwright report with screenshots and traces on failure
- **CI/CD Ready** — GitHub Actions workflow
- **Viewport testing** — Desktop, tablet, and mobile resize verification
- **Tag-based filtering** — `@smoke`, `@regression`, `@login`, `@cart`, `@checkout`

## Setup

```bash
# Clone and install
git clone https://github.com/Neetha-BM/playwright-test-framework.git
cd playwright-test-framework
git checkout typescript
npm install

# Install browsers
npx playwright install chromium
```

## Running Tests

```bash
# Run all tests
npx playwright test

# Run smoke tests only
npx playwright test --grep "@smoke"

# Run headed (visible browser)
npx playwright test --headed

# Run specific browser
npx playwright test --project=chromium
npx playwright test --project=firefox
npx playwright test --project=webkit

# Open interactive UI mode
npx playwright test --ui

# View HTML report
npx playwright show-report
```

## Test Coverage

| Feature       | Tests | Scenarios                                              |
|---------------|-------|--------------------------------------------------------|
| Login         | 5     | Valid login, locked user, empty fields, invalid creds  |
| Inventory     | 7     | Product display, sorting (4 options), add/remove cart  |
| Cart          | 4     | View items, remove items, continue shopping, checkout  |
| Checkout      | 7     | Complete flow, validation, cancel, back to products    |
| Browser       | 4     | Maximized launch, desktop, tablet, mobile viewports    |
| **Total**     | **27**|                                                        |

## Technologies

- **TypeScript 5** — Strongly typed test code
- **Playwright** — Modern cross-browser automation
- **Node.js 22** — Runtime
- **GitHub Actions** — CI/CD

> **Python branch:** The `main` branch contains the equivalent framework in Python + pytest with Allure reporting.

## Author

Neetha B. — Senior QA Automation Engineer
