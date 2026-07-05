import { Page } from '@playwright/test';
import { BasePage } from './BasePage';

export class InventoryPage extends BasePage {
  private readonly inventoryItem = "[data-test='inventory-item']";
  private readonly sortDropdown = "[data-test='product-sort-container']";
  private readonly cartBadge = "[data-test='shopping-cart-badge']";
  private readonly cartLink = "[data-test='shopping-cart-link']";
  private readonly burgerMenu = '#react-burger-menu-btn';
  private readonly logoutLink = '#logout_sidebar_link';

  constructor(page: Page) {
    super(page);
  }

  async getItemCount(): Promise<number> {
    return this.page.locator(this.inventoryItem).count();
  }

  async getItemNames(): Promise<string[]> {
    return this.page.locator("[data-test='inventory-item-name']").allTextContents();
  }

  async getItemPrices(): Promise<number[]> {
    const texts = await this.page.locator("[data-test='inventory-item-price']").allTextContents();
    return texts.map(p => parseFloat(p.replace('$', '')));
  }

  async addItemToCartByName(name: string): Promise<this> {
    const id = name.toLowerCase().replace(/ /g, '-');
    await this.page.click(`[data-test='add-to-cart-${id}']`);
    await this.pause();
    return this;
  }

  async removeItemFromCartByName(name: string): Promise<this> {
    const id = name.toLowerCase().replace(/ /g, '-');
    await this.page.click(`[data-test='remove-${id}']`);
    await this.pause();
    return this;
  }

  async getCartBadgeCount(): Promise<number> {
    const visible = await this.page.isVisible(this.cartBadge);
    if (!visible) return 0;
    const text = await this.page.textContent(this.cartBadge);
    return parseInt(text ?? '0', 10);
  }

  async goToCart(): Promise<this> {
    await this.page.click(this.cartLink);
    await this.pause();
    return this;
  }

  async sortBy(value: string): Promise<this> {
    await this.page.selectOption(this.sortDropdown, value);
    await this.pause();
    return this;
  }

  async logout(): Promise<this> {
    await this.page.click(this.burgerMenu);
    await this.page.click(this.logoutLink);
    await this.pause();
    return this;
  }
}
