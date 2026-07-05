import { test, expect } from '@playwright/test';
import { LoginPage } from '@pages/LoginPage';
import { InventoryPage } from '@pages/InventoryPage';
import { CartPage } from '@pages/CartPage';
import { VALID_USER, PASSWORD } from '@utils/config';

test.describe('Cart', () => {

  test.beforeEach(async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await loginPage.login(VALID_USER, PASSWORD);
    await page.waitForURL(/inventory/);
  });

  test('added items appear in cart @smoke @cart', async ({ page }) => {
    const inventoryPage = new InventoryPage(page);
    await inventoryPage.addItemToCartByName('Sauce Labs Backpack');
    await inventoryPage.goToCart();
    const cartPage = new CartPage(page);
    expect(await cartPage.getCartItemCount()).toBe(1);
  });

  test('remove item from cart @cart', async ({ page }) => {
    const inventoryPage = new InventoryPage(page);
    await inventoryPage.addItemToCartByName('Sauce Labs Backpack');
    await inventoryPage.goToCart();
    const cartPage = new CartPage(page);
    await cartPage.removeItemByName('Sauce Labs Backpack');
    expect(await cartPage.getCartItemCount()).toBe(0);
  });

  test('continue shopping returns to inventory @cart', async ({ page }) => {
    const inventoryPage = new InventoryPage(page);
    await inventoryPage.goToCart();
    const cartPage = new CartPage(page);
    await cartPage.continueShopping();
    await expect(page).toHaveURL(/inventory/);
  });

  test('checkout button navigates to checkout @cart', async ({ page }) => {
    const inventoryPage = new InventoryPage(page);
    await inventoryPage.addItemToCartByName('Sauce Labs Backpack');
    await inventoryPage.goToCart();
    const cartPage = new CartPage(page);
    await cartPage.proceedToCheckout();
    await expect(page).toHaveURL(/checkout-step-one/);
  });
});
