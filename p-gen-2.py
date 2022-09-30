import random
import rich
import string
import banner
import time
import os, sys

from rich.console import Console
from rich.prompt import Prompt
from config_banner import text

console = Console()

banner.banner(text=text)

console.print('[red]GITHUB:[/] [white]https://github.com/void990/P-GEN-2\n[red]VERSION:[/] [bold white]1.0\n')

def GenerationPasswords():
    try:
        length = Prompt.ask("[red]Password length?[/]", default='50')
 
        many = Prompt.ask("[purple]How many passwords?[/]", default='10')
        
        delay = Prompt.ask("[magenta]Generation delay[/]", default='0')
                         
    except Exception as error:
           console.print(f'[bold red][!] ERROR![/]: {error}')


    for i in range(int(many)):
        try:
           generate = "".join(random.sample(string.ascii_letters, k = int(length)))
           time.sleep(int(delay))
           console.print(f"[red]PASSWORD[/][white][{i}]:[/] [bold white]{generate}[/]")

        except KeyboardInterrupt:
              console.print(f'\n[italic magenta]GENERATION[/] [bold red]STOP![/] [bold white]Count [{i}]\n') 
              sys.exit()
              
GenerationPasswords()
