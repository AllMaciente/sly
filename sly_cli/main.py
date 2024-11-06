import os
import sys

# Adiciona o diretório atual ao sys.path
sys.path.append(os.path.dirname(__file__))
gi = __import__("req_gitignore")
from rich import print
from typer import Argument, Context, Exit, Option, Typer

app = Typer()

__version__ = "0.0.1"


def version(arg):
    if arg:
        print(__version__)
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def callback(
    ctx: Context,
    version: bool = Option(
        False,
        "--version",
        "-v",
        "--versao",
        callback=version,
        is_eager=True,
        is_flag=True,
        case_sensitive=False,
    ),
):
    if ctx.invoked_subcommand:
        return


@app.command()
def test():
    print("test")


@app.command()
def gitignore(lang: str = Argument(...), path: str = Argument(os.getcwd())):
    gi.generate(path, lang)


if __name__ == "__main__":
    app()
