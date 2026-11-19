// Entry program for the make.fun bounty "Post a GTA 6 meme on X"
// (gta6-meme-x-01, program/v1, Node 22).
//
// The entry is the X post itself; the house reads the post from X and
// judges it there. This program's only job is to hand the post's address
// to the grader: it copies POST.json from this repository to the output
// directory, byte for byte, and prints nothing on success.
//
// It uses the Node standard library only, touches no network and no wall
// clock, and writes the same bytes on every run.

import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));

const botDir = process.env.MAKEFUN_BOT_DIR
  ? resolve(process.env.MAKEFUN_BOT_DIR)
  : here;
const outDir = process.env.MAKEFUN_OUTPUT_DIR
  ? resolve(process.env.MAKEFUN_OUTPUT_DIR)
  : "/output";

const source = join(botDir, "POST.json");
const target = join(outDir, "POST.json");

if (!existsSync(source)) {
  process.stderr.write(`POST.json not found at ${source}\n`);
  process.exit(1);
}

// Fail fast on a malformed POST.json: the gate refuses one that does not
// read as a JSON object, so catch that here instead of at grading time.
try {
  const parsed: unknown = JSON.parse(readFileSync(source, "utf8"));
  if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
    throw new Error("POST.json is not a JSON object");
  }
} catch (err) {
  process.stderr.write(`POST.json is not valid JSON: ${String(err)}\n`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
