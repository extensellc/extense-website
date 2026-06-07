/*
  Generates the default Open Graph share card -> public/images/og-default.png
  (1200x630). Run with: node scripts/generate-og.mjs

  Pure-vector brand mark (stacked amber squares) + corner registration marks
  + EXTENSE wordmark + tagline, on the warm brand background. Re-run to
  regenerate after edits.
*/
import sharp from "sharp";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const __dirname = dirname(fileURLToPath(import.meta.url));
const out = resolve(__dirname, "../public/images/og-default.png");

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="amber" x1="30" y1="10" x2="170" y2="160" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fcd34d"/>
      <stop offset="50%" stop-color="#fde047"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="630" fill="#FAF7F2"/>

  <!-- corner registration marks -->
  <g stroke="#d97706" stroke-width="3" fill="none" stroke-linecap="square">
    <path d="M40 74 L40 40 L74 40"/>
    <path d="M1126 40 L1160 40 L1160 74"/>
    <path d="M40 556 L40 590 L74 590"/>
    <path d="M1126 590 L1160 590 L1160 556"/>
  </g>

  <!-- brand mark (stacked squares), scaled + centered -->
  <g transform="translate(477,108) scale(1.23)">
    <rect x="60" y="10" width="110" height="110" rx="4" fill="none" stroke="url(#amber)" stroke-width="5"/>
    <rect x="30" y="60" width="100" height="100" rx="4" fill="none" stroke="url(#amber)" stroke-width="5"/>
  </g>

  <!-- wordmark -->
  <text x="600" y="392" text-anchor="middle"
    font-family="Montserrat, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    font-weight="300" letter-spacing="16" font-size="58" fill="#1a1817">EXTENSE</text>

  <!-- amber accent rule -->
  <rect x="540" y="420" width="120" height="2" fill="#f59e0b"/>

  <!-- tagline -->
  <text x="600" y="472" text-anchor="middle"
    font-family="'Source Serif 4', 'Source Serif Pro', Georgia, 'Times New Roman', serif"
    font-size="32" fill="#4a4540">Content engineering for documentation that has to be right.</text>
</svg>`;

await sharp(Buffer.from(svg)).png().toFile(out);
console.log("wrote", out);
