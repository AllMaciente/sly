# Sly - Seu Assistente Virtual Inteligente

**Sly** é um assistente virtual baseado em inteligência artificial, projetado para simplificar suas tarefas diárias e oferecer soluções rápidas e precisas. Além das funcionalidades avançadas de IA, Sly também conta com recursos interessantes e personalizados para tornar seu dia mais eficiente. Com uma interface de linha de comando intuitiva, ele está aqui para ajudar em uma variedade de tarefas de forma prática e inovadora.

## Por que "Sly"?

| **Sly** é inspirado em Sylvester "Sly" Dodd da série _Scorpion_, uma das minhas séries favoritas. | <img src="https://static.wikia.nocookie.net/scorpion2011/images/2/27/Sylvester.png/revision/latest?cb=20170506031456" width="150"/> |
| :------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |

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

Isso deve cobrir tanto o caso de instalação pelo usuário final (usando os arquivos de Releases) quanto instruções para quem deseja construir o pacote manualmente.
