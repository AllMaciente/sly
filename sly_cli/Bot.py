import os

import google.generativeai as genai
from rich import print
from rich.console import Console
from rich.markdown import Markdown

error_console = Console(stderr=True, style="bold red")
console = Console()


class gemini:
    def __init__(self):
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not self.GOOGLE_API_KEY:
            error_console(
                "Erro: GOOGLE_API_KEY não encontrada nas variáveis de ambiente!"
            )
            return
        # Configurar o modelo
        genai.configure(api_key=self.GOOGLE_API_KEY)

        # Iniciar um novo chat
        model = genai.GenerativeModel("gemini-pro")
        self.chat = model.start_chat(history=[])

    def Msg(self, message):
        try:

            response = self.chat.send_message(message)

            md = Markdown(response.text)

            return md

        except Exception as e:
            error_console.print(f"\nErro ao processar a mensagem: {str(e)}")
            return

    def Chat(self):

        print("Chatbot iniciado! Digite [yellow]'exit()'[/] para encerrar.")

        while True:
            # Obtém a entrada do usuário
            user_input = input("\n>>> ")

            # Verifica se o usuário quer sair
            if user_input.lower() == "exit()":
                print("Encerrando o chat...")
                break

            try:

                response = self.Msg(user_input)

                print("\nSly:", response)

            except Exception as e:
                error_console.print(f"\nErro ao processar a mensagem: {str(e)}")
