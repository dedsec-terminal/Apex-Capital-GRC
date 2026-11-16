const assert = require('node:assert/strict');
const path = require('node:path');
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
(async () => {
  const browser = await chromium.launch({headless:true});
  const page = await browser.newPage({viewport:{width:1440,height:1000}});
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.setDefaultTimeout(60000);
  await page.goto(process.env.LAB_URL || 'http://127.0.0.1:8766/site/', {waitUntil:'domcontentloaded',timeout:60000});
  await page.locator('.risk-card').last().waitFor();
  assert.equal(await page.locator('.risk-card').count(), 8);
  assert.equal(await page.locator('.test-row').count(), 8);
  assert.equal(await page.locator('.test-state').filter({hasText:'PLANNED'}).count(), 8);
  await page.locator('#chapter-explorer .chapter-group').last().waitFor();
  assert.equal(await page.locator('#chapter-explorer .chapter-group').count(), 13);
  assert.equal(await page.locator('#chapter-explorer li a').count(), 32);
  assert.equal(await page.locator('.featured-card').count(), 3);
  assert.equal(await page.locator('img[src*="assets/diagrams/"]').count(), 6);
  assert.equal(await page.locator('img').evaluateAll(images => images.every(i => i.complete && i.naturalWidth > 0)), true);
  const homeUrl = page.url();
  const chapters = await page.locator('#chapter-explorer li a').evaluateAll(links => links.map(a => a.href));
  for (const url of chapters) {
    const response = await page.request.get(url);
    assert.equal(response.status(), 200, `Chapter did not load: ${url}`);
  }
  for (const url of await page.locator('.download-card').evaluateAll(links => links.map(a => a.href))) {
    const response = await page.request.get(url);
    assert.equal(response.status(), 200);
    const body = await response.body();
    assert.equal(body.subarray(0,2).toString(), 'PK', 'DOCX must be a valid ZIP container');
    assert.ok(body.length > 10000);
  }
  await page.locator('[data-filter="admin"]').click();
  assert.equal(await page.locator('.flow-list li:visible').count(), 2);
  await page.locator('[data-filter="denied"]').click();
  assert.equal(await page.locator('.flow-list li:visible').count(), 1);
  await page.locator('[data-filter="all"]').click();
  await page.screenshot({path:path.resolve(__dirname,'../site/assets/desktop-preview.png'),fullPage:true});
  await page.setViewportSize({width:390,height:844});
  await page.screenshot({path:path.resolve(__dirname,'../site/assets/mobile-preview.png'),fullPage:true});
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1),true);
  await page.locator('.menu-toggle').click();
  assert.equal(await page.locator('.menu-toggle').getAttribute('aria-expanded'), 'true');
  await page.locator('#primary-nav a').first().click();
  assert.equal(await page.locator('.menu-toggle').getAttribute('aria-expanded'), 'false');
  await page.goto(new URL('report/09-Testing-and-Validation/capability-evaluation.html', homeUrl).href);
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), true);
  await page.locator('#search').fill('containment');
  await page.locator('#results a').first().waitFor();
  const resultUrl = await page.locator('#results a').first().getAttribute('href');
  assert.equal((await page.request.get(new URL(resultUrl, page.url()).href)).status(), 200);
  await page.locator('#results a').first().click();
  await page.locator('.article h1').first().waitFor();
  assert.deepEqual(errors,[]);
  await browser.close();
  console.log('Publication browser checks passed: 32 chapters, 6 diagrams, 2 DOCX downloads, search, filters, mobile navigation, 8 risks and 8 planned scenarios.');
})().catch(error=>{console.error(error);process.exit(1);});
