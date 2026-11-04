// Authoring-time rendering of our own Mermaid sources. No website automation.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const args = process.argv.slice(2);
const options = Object.fromEntries(
  Array.from({ length: args.length / 2 }, (_, i) => [args[i * 2], args[i * 2 + 1]]),
);
if (!options["--playwright"]) {
  throw new Error("Provide --playwright PATH to an existing Playwright 1.62.1 module.");
}
const { chromium } = require(path.resolve(options["--playwright"]));
const toolDir = path.dirname(fileURLToPath(import.meta.url));
const out = path.resolve(toolDir, "../dist/diagrams");
const manifestPath = path.join(out, "manifest.json");
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const libraryPath = path.join(toolDir, "vendor/mermaid-10.9.3.min.js");
const configText = fs.readFileSync(path.join(toolDir, "mermaid-config.json"), "utf8");
const config = JSON.parse(configText);
const engineHash = crypto
  .createHash("sha256")
  .update(fs.readFileSync(libraryPath))
  .update(configText)
  .digest("hex");
const browser = await chromium.launch({ headless: true, channel: "msedge" });
const results = [];
try {
  const page = await browser.newPage({
    viewport: { width: 1800, height: 1400 },
    deviceScaleFactor: 1.5,
  });
  await page.setContent(
    '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>body{margin:0;background:white;font-family:"Microsoft YaHei",sans-serif}#chart{display:inline-block;padding:20px;background:#fff}svg{display:block;max-width:none!important}</style><div id="chart"></div></html>',
  );
  await page.addScriptTag({ path: libraryPath });
  await page.evaluate((value) => mermaid.initialize(value), config);
  for (const [index, item] of manifest.diagrams.entries()) {
    const sourcePath = path.join(out, item.id + ".mmd");
    const svgPath = path.join(out, item.id + ".svg");
    const pngPath = path.join(out, item.id + ".png");
    const source = fs.readFileSync(sourcePath, "utf8").replace(/\r\n/g, "\n");
    const sourceHash = crypto.createHash("sha256").update(source).digest("hex");
    if (
      item.renderedSourceHash === sourceHash &&
      item.engineHash === engineHash &&
      fs.existsSync(svgPath) &&
      fs.existsSync(pngPath)
    ) {
      results.push({ id: item.id, cached: true, width: item.width, height: item.height });
      continue;
    }
    const rendered = await page.evaluate(
      async ({ source, index }) => {
        await mermaid.parse(source);
        const { svg } = await mermaid.render("researchFigure" + index, source);
        const host = document.getElementById("chart");
        host.innerHTML = svg;
        await document.fonts.ready;
        const element = host.querySelector("svg");
        const view = element.viewBox.baseVal;
        element.setAttribute("width", String(Math.ceil(view.width)));
        element.setAttribute("height", String(Math.ceil(view.height)));
        const bounds = element.getBoundingClientRect();
        const textOverflow = [...element.querySelectorAll("text")].filter((text) => {
          const r = text.getBoundingClientRect();
          return r.width > 0 &&
            (r.left < bounds.left - 4 || r.right > bounds.right + 4 ||
             r.top < bounds.top - 4 || r.bottom > bounds.bottom + 4);
        }).map((text) => text.textContent);
        return {
          svg: element.outerHTML,
          width: Math.ceil(view.width),
          height: Math.ceil(view.height),
          textOverflow,
        };
      },
      { source, index },
    );
    if (!rendered.svg.includes("<svg") || rendered.svg.includes("Syntax error")) {
      throw new Error("Invalid Mermaid result: " + item.id);
    }
    if (rendered.textOverflow.length) {
      throw new Error("Text leaves SVG bounds in " + item.id + ": " + rendered.textOverflow.join(" / "));
    }
    fs.writeFileSync(svgPath, rendered.svg);
    await page.setViewportSize({
      width: Math.max(1100, rendered.width + 60),
      height: Math.max(800, rendered.height + 60),
    });
    await page.locator("#chart").screenshot({ path: pngPath });
    Object.assign(item, {
      width: rendered.width,
      height: rendered.height,
      renderedSourceHash: sourceHash,
      engineHash,
      svg: "diagrams/" + item.id + ".svg",
      png: "diagrams/" + item.id + ".png",
      source: "diagrams/" + item.id + ".mmd",
      rendered: true,
    });
    results.push({ id: item.id, width: item.width, height: item.height, parsed: true });
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + "\n");
    process.stdout.write(JSON.stringify(results.at(-1)) + "\n");
  }
} finally {
  await browser.close();
}
process.stdout.write(JSON.stringify({ diagrams: results.length, engine: "Mermaid 10.9.3" }) + "\n");
