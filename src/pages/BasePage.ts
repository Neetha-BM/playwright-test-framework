import { Page } from '@playwright/test';
import { DEMO_PAUSE_MS } from '@utils/config';

export class BasePage {
  constructor(protected page: Page) {}

  async navigate(url: string): Promise<void> {
    await this.page.goto(url);
    // Brief pause so the page is visible before the next action
    await this.page.waitForTimeout(DEMO_PAUSE_MS);
  }

  async pause(): Promise<void> {
    await this.page.waitForTimeout(DEMO_PAUSE_MS);
  }

  getTitle(): Promise<string> {
    return this.page.title();
  }

  getUrl(): string {
    return this.page.url();
  }
}
