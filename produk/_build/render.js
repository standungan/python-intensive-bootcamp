// node render.js in.html out.pdf  — mencetak HTML ke PDF dengan Chromium (Playwright)
const { chromium } = require('playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const pg = await b.newPage();
  await pg.goto('file://' + require('path').resolve(inp), { waitUntil: 'load' });
  await pg.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, outline: true, tagged: true });
  await b.close();
})();
