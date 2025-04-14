import requests
import os
from rich.console import Console
from rich import print

console = Console()

os.system("clear")

print('''
         █████╗ ███╗   ██╗ █████╗ ███████╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
        ██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
        ███████║██╔██╗ ██║███████║███████╗███████╗█████╗  ███████║██████╔╝██║     ███████║
        ██╔══██║██║╚██╗██║██╔══██║╚════██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
        ██║  ██║██║ ╚████║██║  ██║███████║███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
        ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
''')


def scan_paths():
    # التحقق من صحة الرابط
    while True:
        url = console.input("[bold green]Enter link (e.g., https://example.com): [/]").strip()
        if url:
            break
        console.print("[bold red][!] You must enter a valid URL![/]")

    # حذف / من نهاية الرابط إذا موجود
    if url.endswith('/'):
        url = url[:-1]

    wordlist_path = "common.txt"
    
    if not os.path.isfile(wordlist_path):
        console.print(f"[red][!] File '{wordlist_path}' not found.[/]")
        return

    with open(wordlist_path, "r") as file:
        paths = file.read().splitlines()

    console.print(f"\n[bold blue]Starting scan on: {url}[/]\n")

    for path in paths:
        full_url = f"{url}/{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                console.print(f"[bold green][+] Found:[/] {full_url} [bold green]| Status: 200[/]")
            else:
                console.print(f"[yellow][-] Not Found:[/] {full_url} | Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            console.print(f"[red][!] Error accessing {full_url} :[/] {e}")

scan_paths()


