import requests
from rich.console import Console
import os

os.system("clear")
print('''
\033[91m
          ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
          ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
          ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║     ██║   ██║██║  ██║█████╗  
          ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██║   ██║██║  ██║██╔══╝  
          ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗╚██████╔╝██████╔╝███████╗
          ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                        \033[0m
''')


console = Console()

def status_code():
    urls = []
    while True:
        url = console.input("[bold green]Enter a Link (or type '[yellow]done[/]' to finish)> [/] ")
        if url.lower() == 'done':
            break
        urls.append(url)

    console.print("\n[bold cyan]Checking status of entered URLs...\n[/]")
    for x in urls:
        try:
            response = requests.get(x)
            if response.status_code == 200:
                console.print(f"[+] {x} is [bold green]UP[/] (200)")
            else:
                console.print(f"[!] {x} returned status code [yellow]{response.status_code}[/]")
        except requests.exceptions.RequestException:
            console.print(f"[-] {x} is [bold red]DOWN[/]")

    console.print("\n[bold magenta]Scan complete. Press Enter to exit...[/]")
    input()

status_code()
