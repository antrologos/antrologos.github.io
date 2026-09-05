import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Manual do Transcritorio. Markdown, e nao um .astro por capitulo: a
// prosa muda toda semana, e obrigar cada capitulo a virar <section
// class="..."> garante deriva de CSS. O layout Manual.astro cuida da
// aparencia; os .md so tem conteudo.
//
// O ARQUIVO nomeia a URL (estudio.md -> /pt/manual/estudio/), e a ordem
// de leitura vem do campo `ordem`. Isso permite reordenar capitulos sem
// mexer nas URLs — importante porque o outDir do build e commitado e nao
// e limpo: uma URL antiga sobrevive para sempre depois de indexada.
const manual = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/manual/pt' }),
  schema: z.object({
    titulo: z.string(),
    descricao: z.string(),
    ordem: z.number(),
  }),
});

export const collections = { manual };
