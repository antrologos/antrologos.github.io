#!/usr/bin/env node
// Updates site-src/src/data/version.json with the latest Transcritorio
// version on PyPI (the official channel since v0.2.0), or with the
// version passed as CLI argument.
//
// Usage:
//   npm run update-version            # fetches latest from PyPI
//   npm run update-version -- 0.2.1   # sets explicitly
//   npm run release                   # updates version + rebuilds site

import { writeFileSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const versionFile = resolve(__dirname, '..', 'src', 'data', 'version.json');

async function fetchLatest() {
  // PyPI, not GitHub releases: releases/latest ignores prereleases and
  // still points at the retired standalone channel (v0.1.8).
  const url = 'https://pypi.org/pypi/transcritorio/json';
  const res = await fetch(url, { headers: { 'User-Agent': 'transcritorio-site-updater' } });
  if (!res.ok) throw new Error(`PyPI API ${res.status}`);
  const data = await res.json();
  if (!data.info || !data.info.version) throw new Error('No info.version in response');
  return String(data.info.version);
}

async function main() {
  const argVersion = process.argv[2];
  let version;
  if (argVersion && argVersion.trim() !== '') {
    version = argVersion.trim().replace(/^v/, '');
    console.log(`Using version from arg: ${version}`);
  } else {
    console.log('Fetching latest release from GitHub...');
    version = await fetchLatest();
    console.log(`Latest release: ${version}`);
  }

  const current = JSON.parse(readFileSync(versionFile, 'utf-8'));
  if (current.version === version) {
    console.log(`version.json already at ${version}, nothing to do.`);
    return;
  }

  writeFileSync(versionFile, JSON.stringify({ version }, null, 2) + '\n', 'utf-8');
  console.log(`Updated version.json: ${current.version} -> ${version}`);
}

main().catch((err) => {
  console.error('Failed:', err.message);
  process.exit(1);
});
