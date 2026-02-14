#!/usr/bin/env python3
import sys
from rich.console import Console

console = Console()

class BugBountyMultiAgentSystem:
    def __init__(self):
        console.print("[bold cyan]🎯 BugBounty Multi-Agent IA System[/bold cyan]")
        self.name = "BugBounty IA"

    def show_menu(self):
        console.print(""" 
        [yellow]Opciones:[/yellow] 
        [1] Escanear un objetivo 
        [2] Ver hallazgos 
        [3] Dashboard CLI 
        [4] Iniciar Dashboard Web 
        [5] Salir 
        """)


def main():
    system = BugBountyMultiAgentSystem()
    while True:
        system.show_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "5":
            console.print("[cyan]¡Hasta luego![/cyan]")
            sys.exit(0)
        else:
            console.print("[red]Opción no válida[/red]")

if __name__ == "__main__":
    main()