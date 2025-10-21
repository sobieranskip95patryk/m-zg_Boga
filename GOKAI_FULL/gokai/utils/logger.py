
from rich.console import Console
console = Console()

def info(msg: str):
    console.log(f"[cyan]INFO[/]: {msg}")

def warn(msg: str):
    console.log(f"[yellow]WARN[/]: {msg}")

def error(msg: str):
    console.log(f"[red]ERROR[/]: {msg}")
