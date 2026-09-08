---
titulo: Transcrever
descricao: Você manda e vai fazer outra coisa. O que escolher antes, e o que esperar.
ordem: 4
---

Transcrever é a parte fácil: um clique e uma espera. Marque as gravações com <kbd>☑</kbd> na
lista e clique em **Transcrever**, na barra de cima.

Sem nenhuma marcada, o botão transcreve **todas as que ainda não têm texto** — que costuma
ser o que você quer quando acabou de montar o projeto.

## A setinha ao lado do botão

<figure>
  <img src="/Transcritorio/img/manual/transcrever-menu.png"
       alt="A setinha do botão Transcrever: o motor e a chave de separar falantes." loading="lazy" />
  <figcaption>A setinha do botão Transcrever: o motor e a chave de separar falantes.</figcaption>
</figure>

Ali ficam duas escolhas que vale conhecer:

- **o motor**, isto é, qual modelo vai ouvir o áudio;
- **Separar falantes**, a chave que liga e desliga a identificação de quem fala.

Deixe **Separar falantes** ligada para entrevistas e grupos focais. Desligue para gravações
de uma pessoa só — uma aula, um depoimento corrido: fica mais rápido, e não há nada a
separar. Essa chave é do projeto: fica como você deixou.

## Qual motor

O padrão é o **TAGARELA**, feito para o português falado. Ele é rápido mesmo em computadores
sem placa de vídeo — e é por isso que é o padrão.

Ele só fala português. Para entrevistas em outra língua, escolha um modelo **Whisper**, que é
multilíngue; e confira antes se a língua está certa nas propriedades da entrevista, porque é
ela que decide o resto.

A troca também pode ser feita em **Ferramentas → Configurar transcrição…**. O motor em uso
aparece sempre no canto direito da barra de baixo.

## Quantas pessoas falam

Se você não tiver dito isso nas propriedades, o programa pergunta uma vez, no começo do lote.
A resposta melhora bastante a separação das vozes — é a diferença entre procurar duas pessoas
e adivinhar quantas são. Um grupo focal forçado a dois falantes sai errado.

Em computadores sem placa de vídeo, a mesma janela oferece **separar as vozes agora ou
depois**, com uma estimativa de tempo. Separar depois deixa a transcrição pronta antes;
separar agora entrega tudo de uma vez. Não há resposta errada.

## Enquanto roda

A barra de baixo mostra o que está acontecendo, em qual arquivo, e traz um botão
**Cancelar**. Uma faixa no alto da lista lembra que há um lote em andamento — é por isso que
as ações de análise ficam esperando: elas leem justamente o texto que está sendo escrito.

Dá para usar o computador para outra coisa enquanto isso. Se quiser que o programa pegue mais
leve, **Ferramentas → Configurar transcrição…** tem a opção de usar só metade da máquina.

## Quanto tempo leva

Depende do motor e do computador, e a janela mostra uma estimativa antes de começar. Como
ordem de grandeza: num computador comum, sem placa de vídeo, o TAGARELA transcreve **muito
mais rápido que o tempo real** — uma hora de entrevista sai em alguns minutos. Com placa de
vídeo, mais rápido ainda. O Whisper é bem mais lento em processador: conte com algo perto da
própria duração do áudio.

A separação das vozes leva um tempo parecido com o da transcrição. Nenhuma das duas é "a
etapa demorada": elas custam quase o mesmo.

## Quando termina

A transcrição aparece na lista, pronta para abrir com duplo clique. Se o programa separou as
vozes, ele vai querer saber de quem é cada uma — é o próximo capítulo.

Se algo falhar, a caixa de erro diz o quê e por quê. Os casos comuns estão em
[Quando algo dá errado](/Transcritorio/pt/manual/problemas/).
