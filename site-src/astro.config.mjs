// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://antrologos.github.io',
  base: '/Transcritorio',
  // Output direto na pasta Transcritorio/ do repo pai (publicada pelo GH Pages)
  outDir: '../Transcritorio',
  // Nao apagar arquivos da pasta destino ao buildar (preserva img/, backup, etc.)
  build: {
    assets: 'assets',
  },
  server: {
    port: 4321,
    host: 'localhost',
  },
  integrations: [
    sitemap({
      i18n: {
        defaultLocale: 'pt',
        locales: {
          pt: 'pt-BR',
          en: 'en-US',
        },
      },
    }),
  ],
  i18n: {
    defaultLocale: 'pt',
    locales: ['pt', 'en'],
    routing: {
      prefixDefaultLocale: true,
    },
  },
});
