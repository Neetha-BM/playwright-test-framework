import { test, expect } from '@playwright/test';
import { LoginPage } from '@pages/LoginPage';
import { VALID_USER, PASSWORD } from '@utils/config';

test.describe('Login', () => {

  test('valid credentials redirect to inventory @smoke @login', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await loginPage.login(VALID_USER, PASSWORD);
    await expect(page).toHaveURL(/inventory/);
  });

  test('locked-out user sees error @login', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await loginPage.login('locked_out_user', PASSWORD);
    await loginPage.expectErrorText('locked out');
  });

  test('empty username shows error @login', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await loginPage.login('', PASSWORD);
    await loginPage.expectErrorText('Username is required');
  });

  test('empty password shows error @login', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await loginPage.login(VALID_USER, '');
    await loginPage.expectErrorText('Password is required');
  });

  test('invalid credentials show error @login', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await loginPage.login('wrong_user', 'wrong_pass');
    await loginPage.expectErrorText('do not match');
  });
});
