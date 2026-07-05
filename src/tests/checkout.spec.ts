import { test, expect } from '@playwright/test';
import { LoginPage } from '@pages/LoginPage';
import { InventoryPage } from '@pages/InventoryPage';
import { CartPage } from '@pages/CartPage';
import { CheckoutPage } from '@pages/CheckoutPage';
import { VALID_USER, PASSWORD } from '@utils/config';

test.describe('Checkout', () => {

  test.beforeEach(async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await loginPage.login(VALID_USER, PASSWORD);
    await page.waitForURL(/inventory/);
    const inventoryPage = new InventoryPage(page);
    await inventoryPage.addItemToCartByName('Sauce Labs Backpack');
    await inventoryPage.goToCart();
    const cartPage = new CartPage(page);
    await cartPage.proceedToCheckout();
  });

  test('complete checkout flow @smoke @checkout', async ({ page }) => {
    const checkoutPage = new CheckoutPage(page);
    await checkoutPage.fillShippingInfo('John', 'Doe', 'M5V 3A8');
    await checkoutPage.clickContinue();
    await checkoutPage.clickFinish();
    await checkoutPage.expectOrderComplete();
  });

  test('missing first name shows error @checkout', async ({ page }) => {
    const checkoutPage = new CheckoutPage(page);
    await checkoutPage.fillShippingInfo('', 'Doe', 'M5V 3A8');
    await checkoutPage.clickContinue();
    await checkoutPage.expectErrorVisible();
  });

  test('missing last name shows error @checkout', async ({ page }) => {
    const checkoutPage = new CheckoutPage(page);
    await checkoutPage.fillShippingInfo('John', '', 'M5V 3A8');
    await checkoutPage.clickContinue();
    await checkoutPage.expectErrorVisible();
  });

  test('missing postal code shows error @checkout', async ({ page }) => {
    const checkoutPage = new CheckoutPage(page);
    await checkoutPage.fillShippingInfo('John', 'Doe', '');
    await checkoutPage.clickContinue();
    await checkoutPage.expectErrorVisible();
  });

  test('cancel returns to cart @checkout', async ({ page }) => {
    const checkoutPage = new CheckoutPage(page);
    await checkoutPage.clickCancel();
    await expect(page).toHaveURL(/cart/);
  });

  test('overview shows order total @checkout', async ({ page }) => {
    const checkoutPage = new CheckoutPage(page);
    await checkoutPage.fillShippingInfo('John', 'Doe', 'M5V 3A8');
    await checkoutPage.clickContinue();
    const total = await checkoutPage.getTotal();
    expect(total).toContain('Total:');
  });

  test('back home after order completion @checkout', async ({ page }) => {
    const checkoutPage = new CheckoutPage(page);
    await checkoutPage.fillShippingInfo('John', 'Doe', 'M5V 3A8');
    await checkoutPage.clickContinue();
    await checkoutPage.clickFinish();
    await checkoutPage.goBackHome();
    await expect(page).toHaveURL(/inventory/);
  });
});
