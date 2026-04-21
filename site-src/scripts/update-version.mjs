#!/usr/bin/env node
// Updates site-src/src/data/version.json with the latest Transcritorio release tag,
// or with the version passed as CLI argument.
//
// Usage:
//   npm run update-version            # fetches latest from GitHub API
//   npm run update-version -- 0.1.2   # sets to 0.1.2 explicitly
//   npm run release                   # updates version + rebuilds site

import { writeFileSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const versionFile = resolve(__dirname, '..', 'src', 'data', 'version.json');

async function fetchLatest() {
  const url = 'https://api.github.com/repos/antrologos/Transcritorio/releases/latest';
  const res = await fetch(url, { headers: { 'User-Agent': 'transcritorio-site-updater' } });
  if (!res.ok) throw new Error(`GitHub API ${res.status}`);
  const data = await res.json();
  if (!data.tag_name) throw new Error('No tag_name in response');
  return data.tag_name.replace(/^v/, '');
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
