import os

import requests
from rich import print


def generate(path, lang):
    content = requests.get(
        f"https://raw.githubusercontent.com/github/gitignore/refs/heads/main/{lang}.gitignore"
    )

    try:
        with open(os.path.join(path, ".gitignore"), "w") as f:
            f.write(content.text)
        print(f"Arquivo gerado em {path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
