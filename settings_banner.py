from rich.console import Console
from rich.prompt import Prompt
from config_banner import text
import banner

console = Console()

font = console.input("[red]banner font: ")
text = console.input("[magenta]banner text: ")

file = open("config_banner.py", "w")
file.write(f"font = '{font}'\ntext = '{text}'")
file.close()

console.print('[italic white]EXAMPLE:[/]')

banner.banner(text=text)
