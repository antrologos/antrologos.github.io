---
titulo: Quem fala
descricao: O programa separa as vozes; você diz de quem são. Leva dois minutos por entrevista.
ordem: 5
---

O Transcritório separa as vozes sozinho, mas não sabe os nomes — para ele, existem "Voz 1" e
"Voz 2". Dizer quem é cada uma leva dois minutos e melhora tudo o que vem depois: o
documento final, a busca, os temas.

## A pergunta

<figure>
  <img src="/Transcritorio/img/manual/vozes.png"
       alt="Uma linha por voz, com trechos para ouvir. O nome vale para a transcrição inteira." loading="lazy" />
  <figcaption>Uma linha por voz, com trechos para ouvir. O nome vale para a transcrição inteira.</figcaption>
</figure>

Quando a separação termina, o programa abre **De quem é esta voz?**. Se você não responder na
hora, a pergunta não some: ao abrir aquela transcrição, aparece uma faixa dizendo que as
vozes ainda não foram confirmadas, com o botão **Dar nome às vozes…**. Ele também está em
**Entrevista → Dar nome às vozes…**.

A janela mostra uma linha por voz, com quanto ela fala e alguns trechos para ouvir. Clique no
▶ de um trecho, escute, e escreva quem é. Aceita uma sugestão da lista ou qualquer nome que
você digitar. **O nome vale para a transcrição inteira.**

Se, dentro de uma mesma linha, você ouvir **pessoas diferentes**, o número de falantes está
errado. Cancele, ajuste em **Propriedades**, e refaça a separação — sai muito melhor do que
consertar bloco a bloco depois.

## Vozes que se repetem

A partir da terceira entrevista de um projeto, o programa começa a reconhecer vozes que já
apareceram: a linha vem marcada com "parece ser…" e o nome que você usou antes. É uma
**sugestão** — ele nunca aplica sozinho, e você confirma ou troca. O reconhecimento não
atravessa projetos.

## Trocar o falante de um bloco

Na revisão, o campo **Falante** logo abaixo do texto troca o falante do bloco aberto —
<kbd>Alt+E</kbd> abre essa lista sem tirar a mão do teclado. O botão **Aplicar a todos desta
voz** estende o nome a todos os blocos da mesma voz, e <kbd>Ctrl+Z</kbd> desfaz.

Quando o erro não é o falante, mas **onde um bloco termina**, o conserto é outro — e é um
gesto só. Está em [O Estúdio de Revisão](/Transcritorio/pt/manual/estudio/).

## As trocas de falante suspeitas

Depois de separar as vozes, o programa volta ao áudio e confere as trocas de falante que ele
mesmo propôs. Quando duas vozes vizinhas soam parecidas demais para ter certeza, ele marca
aquele bloco como **Dúvida** e mostra uma faixa dizendo quantos há, com setas ‹ › para
percorrê-los.

Esses são o melhor uso do seu tempo: é onde a máquina está insegura, e quase sempre é ali que
o erro está. <kbd>Alt+Shift+↓</kbd> pula de um para o outro.

## Refazer a separação

**Entrevista → Refazer separação de falantes…** recomeça do zero, com as configurações
atuais. Atenção: isso **descarta as edições** daquela transcrição — o programa guarda uma
cópia antes, em Documentos › Versões anteriores, mas o caminho natural é refazer *antes* de
revisar, não depois.

## Uma pessoa só, ou nenhuma separação

Para gravações de uma pessoa só, desligue **Separar falantes** antes de transcrever: é mais
rápido e não há nada a separar. Se a separação estiver indisponível no computador, o programa
avisa antes de começar e transcreve mesmo assim — o texto sai inteiro, sem divisão por voz.
