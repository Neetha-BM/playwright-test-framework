import { Page } from '@playwright/test';
import { BasePage } from './BasePage';

export class CartPage extends BasePage {
  private readonly cartItem = "[data-test='inventory-item']";
  private readonly continueShoppingButton = "[data-test='continue-shopping']";
  private readonly checkoutButton = "[data-test='checkout']";

  constructor(page: Page) {
    super(page);
  }

  async getCartItemCount(): Promise<number> {
    return this.page.locator(this.cartItem).count();
  }

  async getItemNames(): Promise<string[]> {
    return this.page.locator("[data-test='inventory-item-name']").allTextContents();
  }

  async removeItemByName(name: string): Promise<this> {
    const id = name.toLowerCase().replace(/ /g, '-');
    await this.page.click(`[data-test='remove-${id}']`);
    await this.pause();
    return this;
  }

  async continueShopping(): Promise<this> {
    await this.page.click(this.continueShoppingButton);
    await this.pause();
    return this;
  }

  async proceedToCheckout(): Promise<this> {
    await this.page.click(this.checkoutButton);
    await this.pause();
    return this;
  }
}
