import { test, expect, Browser } from '@playwright/test';
import * as path from 'path';

const LOCAL_APP_URL = `file:///${path.resolve(__dirname, '../../local_app/index.html').replace(/\\/g, '/')}`;
const PAUSE = 1500;

async function doLoginAndLogout(page: any) {
  await page.goto(LOCAL_APP_URL);
  await page.waitForTimeout(PAUSE);
  await page.fill("[data-test='username']", 'demo_user');
  await page.waitForTimeout(PAUSE);
  await page.fill("[data-test='password']", 'demo_pass');
  await page.waitForTimeout(PAUSE);
  await page.click("[data-test='login-button']");
  await page.waitForTimeout(PAUSE);
  await expect(page.locator("[data-test='welcome-message']")).toBeVisible();
  await page.click("[data-test='logout-button']");
  await page.waitForTimeout(PAUSE);
}

async function showViewportLabel(page: any, width: number, height: number) {
  await page.evaluate(({ w, h }: { w: number; h: number }) => {
    const el = document.createElement('div');
    el.style.cssText = `
      position: fixed; bottom: 20px; right: 20px;
      background: #333; color: #fff;
      padding: 10px 16px; font-size: 18px; font-weight: bold;
      border-radius: 6px; z-index: 9999; font-family: monospace;
    `;
    el.textContent = `Viewport: ${w} x ${h}`;
    document.body.appendChild(el);
  }, { w: width, h: height });
  await page.waitForTimeout(PAUSE);
}

test.describe('Browser Window', () => {

  test('window is maximized on launch @smoke', async ({ page }) => {
    const screen = await page.evaluate(() => ({
      width: window.screen.availWidth,
      height: window.screen.availHeight,
    }));
    await doLoginAndLogout(page);
    const outer = await page.evaluate(() => ({
      width: window.outerWidth,
      height: window.outerHeight,
    }));
    expect(outer.width).toBeGreaterThanOrEqual(screen.width * 0.9);
    expect(outer.height).toBeGreaterThanOrEqual(screen.height * 0.9);
  });

  test('resize to desktop 1280x720', async ({ browser }: { browser: Browser }) => {
    const context = await browser.newContext({ viewport: { width: 1280, height: 720 } });
    const page = await context.newPage();
    await doLoginAndLogout(page);
    await showViewportLabel(page, 1280, 720);
    const size = page.viewportSize();
    await context.close();
    expect(size?.width).toBe(1280);
    expect(size?.height).toBe(720);
  });

  test('resize to tablet 768x1024', async ({ browser }: { browser: Browser }) => {
    const context = await browser.newContext({ viewport: { width: 768, height: 1024 } });
    const page = await context.newPage();
    await doLoginAndLogout(page);
    await showViewportLabel(page, 768, 1024);
    const size = page.viewportSize();
    await context.close();
    expect(size?.width).toBe(768);
    expect(size?.height).toBe(1024);
  });

  test('resize to mobile 375x812', async ({ browser }: { browser: Browser }) => {
    const context = await browser.newContext({ viewport: { width: 375, height: 812 } });
    const page = await context.newPage();
    await doLoginAndLogout(page);
    await showViewportLabel(page, 375, 812);
    const size = page.viewportSize();
    await context.close();
    expect(size?.width).toBe(375);
    expect(size?.height).toBe(812);
  });
});
