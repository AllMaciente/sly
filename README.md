# Sly - Seu Assistente Virtual Inteligente

Sly é um assistente virtual baseado em inteligência artificial projetado para simplificar suas tarefas diárias e fornecer respostas rápidas e precisas. Com uma interface de linha de comando

## Por que "Sly"?

<div style="display: flex; ">

<p style="padding:5%"> <strong>Sly</strong> é inspirado em Sylvester "Sly" Dodd da série Scorpion, uma das minhas séries favoritas.</p>

<img src="https://static.wikia.nocookie.net/scorpion2011/images/2/27/Sylvester.png/revision/latest?cb=20170506031456" alt="Sly Dodd" width="150" style="margin-right: 10px;"/>

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

## Contribuindo

Sinta-se à vontade para:

- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## Licença

MIT License
