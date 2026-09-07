---
titulo: O Estúdio de Revisão
descricao: Onde as horas vão. O ciclo de revisão pelo teclado, e como consertar o que a máquina errou.
ordem: 6
---

Transcrever é um clique e uma espera. **Revisar é o trabalho.** Uma hora de
entrevista costuma virar cerca de duzentos blocos de fala, e cada um deles pede
uma decisão sua: está certo? é essa pessoa que fala? a fala começa aqui mesmo?

Este capítulo é o mais longo do manual por um motivo simples: é o único lugar do
programa onde existe uma **habilidade a aprender**, e não só comandos a
encontrar. Quinze minutos aqui se pagam na primeira entrevista.

## A tela

Abra uma entrevista com duplo clique na lista. A janela se divide em três:

- **em cima**, a gravação: os controles, a onda sonora e a régua de tempo;
- **no meio**, a lista de blocos, com o falante e o horário de cada um;
- **embaixo**, o texto do bloco aberto, que é onde você digita.

Clicar no **tempo** de um bloco, ou dar duplo clique na linha dele, leva o áudio
até o começo do bloco. Duplo clique numa palavra do texto leva o áudio **até
aquela palavra** — é o gesto para conferir um nome próprio ou um número sem ficar
arrastando a onda. (Vale quando a transcrição tem tempos por palavra, o que é o
caso dos perfis Padrão e Completo.)

## O ciclo

A revisão é sempre a mesma sequência, repetida duzentas vezes: **ouvir, corrigir,
seguir**. Se cada volta dessas custar duas idas ao mouse, são quatrocentas idas
ao mouse por entrevista. Por isso o ciclo inteiro tem tecla:

<ol class="passos">
<li><strong>Ouça.</strong> <kbd>F4</kbd> toca e pausa. <kbd>F3</kbd> volta ao
começo do bloco e toca de novo — é a tecla que você mais vai usar.</li>

<li><strong>Volte um pouco.</strong> <kbd>Alt+←</kbd> e <kbd>Alt+→</kbd> andam
cinco segundos. Com <kbd>Shift</kbd> junto, andam dois — o passo curto de quem
está conferindo uma palavra.</li>

<li><strong>Corrija</strong> direto no texto. Não precisa salvar: trocar de bloco
já salva.</li>

<li><strong>Siga.</strong> <kbd>Alt+↓</kbd> vai ao próximo bloco levando o áudio
junto e deixando o cursor no texto, pronto para digitar.</li>
</ol>

Se a fala estiver rápida demais, <kbd>F7</kbd> e <kbd>F8</kbd> mudam a velocidade
sem mudar o tom da voz.

## Os blocos marcados para conferir

Depois de separar as vozes, o programa confere as **trocas de falante** que ele
mesmo propôs, ouvindo o áudio dos dois lados da emenda. Quando a troca parece
duvidosa, ele marca o bloco como **Dúvida** na lista e mostra, acima dela, uma
faixa com uma lupa 🔍 dizendo quantos há.

Esses blocos são o melhor uso do seu tempo: são os lugares onde a máquina está
insegura, e quase sempre é ali que o erro está. <kbd>Alt+Shift+↓</kbd> pula
direto de um marcado para o outro, ignorando os demais.

## Quando o texto está certo, mas a divisão está errada

Este é o problema mais comum de uma separação automática, e o que mais custava
tempo antes de existir um gesto para ele.

Acontece assim: um bloco atribuído a **A** contém, a partir de certo ponto, a
fala de **B**. O texto está certo, o falante do começo está certo — o que está
errado é a **fronteira entre os dois blocos**.

> Entrevistadora: *E aí você mudou de bairro? **Mudei, em noventa e oito.***
>
> A segunda frase é da entrevistada, mas ficou no bloco da entrevistadora.

O conserto é um gesto:

1. clique no texto, exatamente onde a outra voz começa;
2. aperte <kbd>Alt+P</kbd>.

O programa divide o bloco ali, dá ao pedaço o **falante do bloco seguinte** e
junta os dois. Um único <kbd>Ctrl+Z</kbd> desfaz tudo.

O falante não é perguntado porque não precisa ser: o bloco vizinho já tem o
certo. É por isso que o mesmo gesto funciona igual numa entrevista com duas
pessoas e num grupo focal com seis.

<kbd>Alt+Shift+P</kbd> é o espelho: passa o **começo** do bloco para o bloco de
cima, para quando o pedaço mal atribuído está no início.

E há um caso que parece exceção mas é regra: **com o cursor na ponta do texto, o
bloco inteiro passa** para o vizinho. É o que você quer quando um bloco curto
inteiro foi atribuído à pessoa errada.

### Quando a fala é de alguém que não está ao lado

Aí não há fronteira a mover — o que está errado é o falante mesmo.
<kbd>Alt+E</kbd> abre a lista de falantes do bloco sem tirar a mão do teclado.

## Juntar e dividir

<kbd>Alt+D</kbd> divide o bloco no ponto do cursor. O *texto* sempre divide ali;
para o *tempo* do corte, o programa segue uma ordem: um clique seu na onda sonora,
dentro do bloco, vale primeiro; senão, o tempo da palavra sob o cursor — exato
quando a transcrição tem tempos por palavra e o texto do bloco não foi reescrito,
aproximado pela palavra mais próxima quando foi; senão, a posição do áudio
pausado dentro do bloco; e, por último, uma estimativa pela posição do cursor no
texto. A barra de baixo diz qual dessas regras valeu.

<kbd>Alt+J</kbd> junta com o bloco seguinte e <kbd>Alt+Shift+J</kbd> com o
anterior. Juntar blocos de falantes diferentes é permitido: o bloco resultante
fica com o falante do bloco de cima, e a barra de baixo diz qual ficou.

## Todos os atalhos

<div class="tabela-rolante">
<table>
<thead><tr><th>Tecla</th><th>O que faz</th></tr></thead>
<tbody>
<tr><td><kbd>F4</kbd></td><td>Toca e pausa</td></tr>
<tr><td><kbd>F3</kbd></td><td>Repete o bloco desde o começo</td></tr>
<tr><td><kbd>Alt+←</kbd> / <kbd>Alt+→</kbd></td><td>Volta e avança 5 segundos</td></tr>
<tr><td><kbd>Alt+Shift+←</kbd> / <kbd>Alt+Shift+→</kbd></td><td>Volta e avança 2 segundos</td></tr>
<tr><td><kbd>F7</kbd> / <kbd>F8</kbd></td><td>Mais devagar / mais rápido</td></tr>
<tr><td><kbd>Alt+↓</kbd> / <kbd>Alt+↑</kbd></td><td>Bloco seguinte / anterior</td></tr>
<tr><td><kbd>Alt+Shift+↓</kbd> / <kbd>Alt+Shift+↑</kbd></td><td>Próximo bloco marcado para conferir / anterior</td></tr>
<tr><td><kbd>F6</kbd></td><td>Passa o foco entre a lista de blocos e o texto</td></tr>
<tr><td><kbd>Alt+D</kbd></td><td>Divide o bloco no cursor</td></tr>
<tr><td><kbd>Alt+J</kbd> / <kbd>Alt+Shift+J</kbd></td><td>Junta com o bloco seguinte / anterior</td></tr>
<tr><td><kbd>Alt+P</kbd></td><td>Passa o fim do bloco para o bloco seguinte</td></tr>
<tr><td><kbd>Alt+Shift+P</kbd></td><td>Passa o começo do bloco para o anterior</td></tr>
<tr><td><kbd>Alt+E</kbd></td><td>Escolhe o falante do bloco</td></tr>
<tr><td><kbd>Ctrl+S</kbd></td><td>Salva a transcrição</td></tr>
<tr><td><kbd>Ctrl+Z</kbd></td><td>Desfaz</td></tr>
<tr><td><kbd>F1</kbd></td><td>Abre a lista de todos os comandos do programa</td></tr>
</tbody>
</table>
</div>

Essa tabela também vive dentro do programa, sempre atualizada: <kbd>F1</kbd>, ou
*Ajuda → Atalhos e comandos*. De lá dá para salvá-la em texto e imprimir.

## Por que a tecla e não o botão

<kbd>Espaço</kbd>, <kbd>Ctrl+←</kbd> e <kbd>Ctrl+→</kbd> também tocam e andam no
áudio — mas só quando o cursor **não** está no texto. Um editor de texto precisa
do espaço para escrever espaço, e das setas com <kbd>Ctrl</kbd> para andar entre
palavras; ele fica com essas teclas antes que o programa as veja.

Por isso o ciclo de revisão inteiro usa a família <kbd>Alt</kbd> e as teclas
<kbd>F</kbd>: são as que atravessam o editor. Você pode revisar uma entrevista
inteira sem tirar as mãos do teclado.
