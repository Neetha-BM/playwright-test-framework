import { Page, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class CheckoutPage extends BasePage {
  private readonly firstNameInput = "[data-test='firstName']";
  private readonly lastNameInput = "[data-test='lastName']";
  private readonly postalCodeInput = "[data-test='postalCode']";
  private readonly continueButton = "[data-test='continue']";
  private readonly cancelButton = "[data-test='cancel']";
  private readonly finishButton = "[data-test='finish']";
  private readonly errorMessage = "[data-test='error']";
  private readonly summaryTotal = "[data-test='total-label']";
  private readonly completeHeader = "[data-test='complete-header']";
  private readonly backHomeButton = "[data-test='back-to-products']";

  constructor(page: Page) {
    super(page);
  }

  async fillShippingInfo(firstName: string, lastName: string, postalCode: string): Promise<this> {
    await this.page.fill(this.firstNameInput, firstName);
    await this.page.fill(this.lastNameInput, lastName);
    await this.page.fill(this.postalCodeInput, postalCode);
    await this.pause();
    return this;
  }

  async clickContinue(): Promise<this> {
    await this.page.click(this.continueButton);
    await this.pause();
    return this;
  }

  async clickFinish(): Promise<this> {
    await this.page.click(this.finishButton);
    await this.pause();
    return this;
  }

  async clickCancel(): Promise<this> {
    await this.page.click(this.cancelButton);
    await this.pause();
    return this;
  }

  async getErrorMessage(): Promise<string | null> {
    return this.page.textContent(this.errorMessage);
  }

  async getTotal(): Promise<string | null> {
    return this.page.textContent(this.summaryTotal);
  }

  async expectOrderComplete(): Promise<void> {
    await expect(this.page.locator(this.completeHeader)).toHaveText('Thank you for your order!');
  }

  async expectErrorVisible(): Promise<void> {
    await expect(this.page.locator(this.errorMessage)).toBeVisible();
  }

  async goBackHome(): Promise<this> {
    await this.page.click(this.backHomeButton);
    await this.pause();
    return this;
  }
}
