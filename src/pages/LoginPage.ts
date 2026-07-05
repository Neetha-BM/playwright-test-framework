import { Page, expect } from '@playwright/test';
import { BasePage } from './BasePage';
import { BASE_URL } from '@utils/config';

export class LoginPage extends BasePage {
  private readonly usernameInput = "[data-test='username']";
  private readonly passwordInput = "[data-test='password']";
  private readonly loginButton = "[data-test='login-button']";
  private readonly errorMessage = "[data-test='error']";

  constructor(page: Page) {
    super(page);
  }

  async open(): Promise<this> {
    await this.navigate(BASE_URL);
    return this;
  }

  async login(username: string, password: string): Promise<this> {
    await this.page.fill(this.usernameInput, username);
    await this.page.fill(this.passwordInput, password);
    await this.page.click(this.loginButton);
    await this.pause();
    return this;
  }

  async getErrorMessage(): Promise<string | null> {
    return this.page.textContent(this.errorMessage);
  }

  async expectErrorVisible(): Promise<void> {
    await expect(this.page.locator(this.errorMessage)).toBeVisible();
  }

  async expectErrorText(text: string): Promise<void> {
    await expect(this.page.locator(this.errorMessage)).toContainText(text);
  }
}
