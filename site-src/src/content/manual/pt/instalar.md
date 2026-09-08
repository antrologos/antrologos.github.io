---
titulo: Instalar
descricao: Alguns minutos, sem senha de administrador. E o que o assistente pergunta na primeira vez.
ordem: 2
---

O Transcritório é gratuito e de código aberto. A instalação não pede senha de administrador e
pode ser repetida quantas vezes você quiser, sem quebrar nada.

## Windows

Baixe o instalador na [página do programa](/Transcritorio/pt/#install) e dê dois cliques. Ele
faz três coisas, mostrando o progresso: instala o **uv** (o gerenciador que baixa o resto),
instala o **FFmpeg** (que lê áudio e vídeo) e baixa o **Transcritório**.

São alguns minutos e cerca de 2,5 GB. Pode deixar a janela trabalhando.

No fim, abra o programa — no primeiro uso ele cria o atalho **Transcritório** na sua área de
trabalho. Se o atalho não aparecer, abra o Prompt de Comando e digite `transcritorio`.

**Se der errado**, a janela mostra as últimas linhas do registro e o caminho do arquivo
completo. A causa mais comum é rede de universidade ou empresa bloqueando downloads: peça à TI
para liberar `pypi.org`, `files.pythonhosted.org`, `github.com` e `astral.sh`.

## macOS e Linux

O suporte existe e funciona, ainda em fase de teste. Os comandos estão em
[instalação](/Transcritorio/pt/#install) — são três linhas no terminal, com Homebrew no macOS
e apt no Linux.

## O assistente do primeiro uso

Na primeira abertura, um assistente baixa os modelos que fazem o trabalho. Ele pergunta três
coisas.

**Qual perfil.** Essencial, Padrão ou Completo. O Padrão atende quase todo mundo: transcreve,
separa as vozes e marca os tempos por palavra. O Essencial é mais leve e dispensa os tempos
por palavra; o Completo acrescenta os recursos de análise. A janela mostra quanto cada um pesa
**no seu computador** e o que ele detectou de hardware. Nada aqui é definitivo: dá para mudar
depois em **Ferramentas → Gerenciar modelos…**.

**Uma conta no Hugging Face.** É de graça, e serve como um "Google Acadêmico de modelos": o
modelo que separa as vozes exige que você tenha uma conta e aceite as condições de uso dele.
O assistente abre as páginas certas nos botões.

**Uma chave de acesso.** Você cola a chave que a sua conta gera. Ela fica guardada no cofre do
seu sistema — o Gerenciador de Credenciais, no Windows —, é usada só para baixar modelos, e
nunca aparece em arquivo nenhum.

Dá para pular o assistente e voltar depois: o programa avisa, na barra de baixo, que os
componentes ainda não estão instalados.

## Espaço em disco

Some o aplicativo (~1,5 GB) com os modelos do perfil escolhido. Na prática, entre 6 e 20 GB,
conforme o perfil. Os modelos ficam fora da pasta dos projetos e são compartilhados por todos
eles — você baixa uma vez só.

## Atualizar e desinstalar

**Ajuda → Verificar atualizações…** mostra o comando a rodar com o programa fechado, e um
botão para copiá-lo. O programa também avisa sozinho, na barra de baixo, quando sai uma versão
nova.

Para desinstalar, `uv tool uninstall transcritorio`. Os seus **projetos não são tocados**, e os
modelos continuam no disco caso você reinstale.

## A versão de teste

Existe um canal de teste (*beta*), instalado **lado a lado** com o estável: os dois podem ficar
abertos ao mesmo tempo, e a janela da beta diz isso no título. É onde as novidades aparecem
primeiro. Só entre nele se quiser ajudar a testar.
