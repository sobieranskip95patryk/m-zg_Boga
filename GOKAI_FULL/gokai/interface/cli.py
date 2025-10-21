
import click
from rich.table import Table
from rich.console import Console
from gokai.core.formula import GOKAIFormula

console = Console()

@click.command()
@click.option("--config", "-c", type=str, default=None, help="Ścieżka do config.yaml")
@click.option("--show", type=click.Choice(["none","values","all"]), default="values")
def main(config, show):
    f = GOKAIFormula(config)
    s = f.S()

    console.rule("[bold magenta]GOK:AI — równanie S")
    console.print(f"[bold]S = (W+M+D+C+A) * E * T = {s:.3f}[/]")

    if show in ("values","all"):
        t = Table(title="Składowe")
        t.add_column("Komponent"); t.add_column("Wartość", justify="right")
        t.add_row("W (Intrinsic)", str(f.W.value()))
        t.add_row("M (Skills)", str(f.M.value()))
        t.add_row("D (Decisions)", str(f.D.value()))
        t.add_row("C (Context)", str(f.C.value()))
        t.add_row("A (Personality)", str(f.A.value()))
        t.add_row("E (Energy)", str(f.E.value()))
        t.add_row("T (Time)", str(f.T.value()))
        console.print(t)

    if show == "all":
        console.print("\n[dim]Opis filozoficzny w docs/[/dim]")

if __name__ == "__main__":
    main()
