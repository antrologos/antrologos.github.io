---
titulo: Quando algo dá errado
descricao: Os avisos que aparecem, o que cada um quer dizer, e o que fazer.
ordem: 9
---

Antes da lista: a **barra de baixo** da janela sempre diz o que está acontecendo e o que
acabou de acontecer. E um comando cinza explica, no balão que aparece ao pousar o mouse, por
que está cinza. Boa parte das dúvidas se resolve olhando para lá.

## "FFmpeg não encontrado"

O FFmpeg é o programa que lê áudio e vídeo; o Transcritório depende dele e ele não veio
junto. A janela traz o comando pronto e um botão para copiar. Cole no Prompt de Comando,
rode, e reabra o Transcritório:

```
winget install Gyan.FFmpeg
```

## "Modelos locais pendentes"

Falta baixar algum componente para a ação que você pediu — a janela **diz qual e quanto pesa**.
Responder que sim inicia o download; ele continua de onde parou se for interrompido.

Se aparecer **"Download anterior inconcluso"**, é isso mesmo: um download foi cortado no meio.
Aceite retomar — o que já veio é aproveitado.

Os botões dessas perguntas aparecem em inglês (*Yes* / *No*): são os botões padrão do sistema,
não uma tradução esquecida.

## "A tarefa terminou com erro"

O botão **Show Details…** abre a causa. Desde a versão de teste atual, ela vem nomeada: qual
componente falhou e por quê — token do Hugging Face ausente ou inválido, termos do modelo não
aceitos, ou falta de conexão.

Se disser que o **Hugging Face recusou o acesso**, vá a **Ferramentas → Gerenciar modelos…** e
confira a chave. Se disser que os **termos não foram aceitos**, abra a página do modelo no
Hugging Face com a mesma conta e aceite as condições.

## "Mídia não encontrada"

A gravação saiu do lugar. O projeto nunca copiou o áudio — ele aponta para onde o arquivo
estava. Devolva-o ao caminho de origem, ou adicione-o de novo ao projeto.

## "Esta pasta não é um projeto do Transcritório"

Você abriu uma pasta comum. Um projeto tem dentro um arquivo `.transcritorio` — escolha esse
arquivo, ou crie um projeto novo em **Projeto → Novo projeto…**.

## Parece travado

A separação de vozes tem uma etapa longa em que a barra anda devagar; é normal. Enquanto
houver texto mudando na barra de baixo, o trabalho está andando. Se quiser parar, o botão
**Cancelar** fica ali ao lado.

## Atualizar, reparar, acelerar

Três itens mostram um comando para você rodar com o **programa fechado**, e um botão para
copiá-lo — eles não executam nada sozinhos:

- **Ajuda → Verificar atualizações…** — a versão nova, quando existe, também é anunciada na
  barra de baixo ao abrir o programa.
- **Ajuda → Reparar instalação…** — reconstrói a parte técnica. **Seus projetos, áudios,
  transcrições e modelos não são afetados.**
- **Ferramentas → Instalar aceleração NVIDIA (CUDA)…** — só vale a pena se o computador tiver
  uma placa NVIDIA.

## Nada disso resolveu

O registro técnico dos downloads fica em
`%LOCALAPPDATA%\Transcritorio\download_diagnostic.log`, e é ele que costuma ter a causa real.

Problemas podem ser relatados em
[github.com/antrologos/Transcritorio/issues](https://github.com/antrologos/Transcritorio/issues).
Conte o que você fez, o que esperava e o que aconteceu — e anexe esse registro, se puder.

## O que nunca acontece

Nenhum áudio, nenhuma transcrição e nenhum nome sai do seu computador. O programa só usa a
internet para baixar os modelos e para conferir se há versão nova.
