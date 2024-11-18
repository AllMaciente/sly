# Sly - Seu Assistente Virtual Inteligente

**Sly** é um assistente virtual baseado em inteligência artificial, projetado para simplificar suas tarefas diárias e oferecer soluções rápidas e precisas. Além das funcionalidades avançadas de IA, Sly também conta com recursos interessantes e personalizados para tornar seu dia mais eficiente. Com uma interface de linha de comando intuitiva, ele está aqui para ajudar em uma variedade de tarefas de forma prática e inovadora.

## Por que "Sly"?

| **Sly** é inspirado em Sylvester "Sly" Dodd da série _Scorpion_, uma das minhas séries favoritas. | <img src="https://static.wikia.nocookie.net/scorpion2011/images/2/27/Sylvester.png/revision/latest?cb=20170506031456" width="150"/> |
| :------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |

## Instalação do Pacote sly

Este repositório contém o código-fonte e os arquivos necessários para construir e instalar o pacote sly. O pacote pode ser instalado localmente ou via pipx a partir dos arquivos disponibilizados nos Releases.
Requisitos

</div>

## Configuração da Chave API

Antes de executar o chatbot, você precisa configurar sua chave API do [`Gemini`](https://aistudio.google.com/app/apikey). Escolha o método adequado para seu sistema operacional:

### Linux/macOS

#### Temporário (válido apenas para a sessão atual do terminal):

```bash
export GOOGLE_API_KEY='sua-chave-api'
```

#### Permanente:

1. Abra o arquivo de configuração do seu shell:

   - Para bash:

   ```bash
   nano ~/.bashrc
   ```

   - Para zsh:

   ```bash
   nano ~/.zshrc
   ```

2. Adicione a linha abaixo no final do arquivo:

   ```bash
   export GOOGLE_API_KEY='sua-chave-api'
   ```

3. Salve o arquivo e recarregue as configurações:
   - Para bash:
   ```bash
   source ~/.bashrc
   ```
   - Para zsh:
   ```bash
   source ~/.zshrc
   ```

### Windows

#### Temporário (via PowerShell):

```powershell
$env:GOOGLE_API_KEY = 'sua-chave-api'
```

#### Permanente (via Interface Gráfica):

1. Pressione `Windows + R`
2. Digite `sysdm.cpl` e pressione Enter
3. Vá para a aba "Avançado"
4. Clique em "Variáveis de Ambiente"
5. Em "Variáveis do Sistema", clique em "Novo"
6. Nome da variável: `GOOGLE_API_KEY`
7. Valor da variável: `sua-chave-api`
8. Clique em "OK" para salvar

## Instalação do Pacote sly

Este repositório contém o código-fonte e os arquivos necessários para construir e instalar o pacote sly. O pacote pode ser instalado localmente ou via pipx a partir dos arquivos disponibilizados nos Releases.
Requisitos

    Python 3.10 ou superior
    pip ou pipx para gerenciamento de pacotes

Como Instalar Usando pipx

    Baixe o arquivo .whl ou .tar.gz da seção Releases deste repositório.

    Instale o pacote com pipx:

pipx install caminho/para/sly-0.0.1-py3-none-any.whl

ou, se estiver usando o .tar.gz:

    pipx install caminho/para/sly-0.0.1.tar.gz

O pipx isola o pacote em um ambiente virtual separado, evitando conflitos com outras dependências instaladas globalmente.
Como Construir o Pacote

Se desejar construir o pacote por conta própria:

    Clone este repositório:

git clone https://github.com/seu-usuario/sly.git
cd sly

Certifique-se de que o Poetry está instalado:

pip install poetry

Construa o pacote:

    poetry build

Os arquivos .whl e .tar.gz serão gerados na pasta dist/.
      

## Contribuindo

Sinta-se à vontade para:

- Reportar bugs
- Sugerir melhorias
- Enviar pull requests


## Licença

MIT License
