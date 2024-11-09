import os
import platform
import sys

from rich import print
from typer import Argument, Context, Exit, Option, Typer

from sly_cli.Bot import gemini
from sly_cli.req_gitignore import generate

app = Typer()

__version__ = "0.0.1"


def get_system_info():
    """
    Gets the operating system information.

    Returns:
        A dictionary containing the operating system name, version, and Linux distribution (if applicable).
    """
    os_name = platform.system()
    os_version = platform.release()

    if os_name == "Linux":
        try:
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.startswith("NAME="):
                        distro_name = line.split("=")[1].strip()
                    elif line.startswith("VERSION_ID="):
                        distro_version = line.split("=")[1].strip()
        except FileNotFoundError:
            return {
                "os_name": os_name,
                "os_version": os_version,
                "distro_name": None,
                "distro_version": None,
            }

        return {
            "os_name": os_name,
            "os_version": os_version,
            "distro_name": distro_name,
            "distro_version": distro_version,
        }
    else:
        return {
            "os_name": os_name,
            "os_version": os_version,
            "distro_name": None,
            "distro_version": None,
        }


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
    generate(path, lang)


@app.command()
def chat():
    chatBot = gemini()
    chatBot.Chat()


@app.command()
def cmd(
    cmd: str = Argument(..., help="descreva qual comando vc quer que ele te mostre")
):
    cmdBot = gemini()
    system = get_system_info()
    if system["os_name"] == "Linux":
        prompt = f'me ajude a gerar um comando para o terminal {system["os_name"]} na distro {system["distro_name"]} para fazer o que estou pedindo entre aspas "{cmd}" com uma pequena explicação antes do que esse comando faz'
    else:
        prompt = f'me ajude a gerar um comando para o terminal {system["os_name"]} para fazer o que estou pedindo entre aspas "{cmd}" com uma pequena explicação antes do que esse comando faz'

    response = cmdBot.Msg(prompt)
    print(response)


if __name__ == "__main__":
    app()
