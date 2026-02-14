#!/usr/bin/env python3
"""
Orquestador principal del sistema multi-agente IA para Bug Bounty
"""

import sys
from rich.console import Console
from rich.table import Table

# Importaciones relativas para cuando se ejecuta como módulo
try:
    from .agents.scanning_agent import ScanningAgent
    from .agents.fuzzing_agent import FuzzingAgent
    from .agents.sqli_agent import SQLiAgent
    from .agents.ai_analysis_agent import AIAnalysisAgent
except ImportError:
    # Fallback para ejecuciones directas si es necesario
    from agents.scanning_agent import ScanningAgent
    from agents.fuzzing_agent import FuzzingAgent
    from agents.sqli_agent import SQLiAgent
    from agents.ai_analysis_agent import AIAnalysisAgent

console = Console()


class BugBountyMultiAgentSystem:
    """Sistema orquestador principal"""
    
    def __init__(self):
        self.scanning_agent = ScanningAgent()
        self.fuzzing_agent = FuzzingAgent()
        self.sqli_agent = SQLiAgent()
        self.ai_agent = AIAnalysisAgent()
        console.print("[bold cyan]🎯 BugBounty Multi-Agent IA System[/bold cyan]")
    
    def show_menu(self):
        """Muestra menú principal"""
        console.print("\n[yellow]Opciones:[/yellow]")
        console.print("[1] Escanear un objetivo (Nmap)")
        console.print("[2] Fuzzing de directorios")
        console.print("[3] Detección de SQL Injection")
        console.print("[4] Análisis de hallazgos con IA")
        console.print("[5] Ver resumen de resultados")
        console.print("[6] Salir")

    def run_scanner(self):
        target = input("Introduce el objetivo (IP o Dominio): ").strip()
        if target:
            self.scanning_agent.execute(target)

    def run_fuzzer(self):
        target = input("Introduce la URL para fuzzing: ").strip()
        if target:
            self.fuzzing_agent.execute(target)

    def run_sqli(self):
        target = input("Introduce la URL para probar SQLi: ").strip()
        if target:
            self.sqli_agent.execute(target)

    def run_ai_analysis(self):
        self.ai_agent.execute("Resultados de escaneo previo...")

    def show_results(self):
        table = Table(title="Resumen de Hallazgos")
        table.add_column("Agente", style="cyan")
        table.add_column("Resultados", style="magenta")
        
        table.add_row("Scanning", str(len(self.scanning_agent.results)))
        table.add_row("Fuzzing", str(len(self.fuzzing_agent.results)))
        table.add_row("SQLi", str(len(self.sqli_agent.results)))
        table.add_row("AI Analysis", str(len(self.ai_agent.results)))
        
        console.print(table)


def main():
    """Función principal"""
    system = BugBountyMultiAgentSystem()
    
    while True:
        system.show_menu()
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1":
            system.run_scanner()
        elif opcion == "2":
            system.run_fuzzer()
        elif opcion == "3":
            system.run_sqli()
        elif opcion == "4":
            system.run_ai_analysis()
        elif opcion == "5":
            system.show_results()
        elif opcion == "6":
            console.print("[cyan]¡Hasta luego![/cyan]")
            sys.exit(0)
        else:
            console.print("[red]Opción no válida[/red]")


if __name__ == "__main__":
    main()
