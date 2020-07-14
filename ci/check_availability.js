const puppeteer = require("puppeteer");
const fs = require("fs");
const dir = "./ci/screenshots";
const url = "http://127.0.0.1/";

if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir);
}

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({
    width: 1920,
    height: 1080,
  });
  try {
    await page.goto(url);
    await page.screenshot({ path: dir + "/login.png" });
    await page.type("#username", "huangbo");
    await page.type("#password", "123456");
    await page.keyboard.press("Enter", { delay: 3000 });
    await page.screenshot({ path: dir + "/index.png" });
  } catch (e) {
    console.log(e.toString());
    process.exit(1);
  } finally {
    await browser.close();
  }
})();