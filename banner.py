import pyfiglet
from config_banner import font

def banner(text: str) -> str:
    banner = pyfiglet.figlet_format(text, font=font)
    return print(banner)
