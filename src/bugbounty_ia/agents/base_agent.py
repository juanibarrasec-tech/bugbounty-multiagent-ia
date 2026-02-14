"""
Clase base para todos los agentes
"""
import json
from datetime import datetime
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Clase base para todos los agentes"""
    
    def __init__(self, name: str):
        self.name = name
        self.results = []
        self.timestamp = datetime.now().isoformat()
    
    def log(self, message: str):
        """Registra un mensaje"""
        print(f"[{self.name}] {message}")
    
    @abstractmethod
    def execute(self, target: str):
        """Ejecuta el agente (debe implementarse en subclases)"""
        pass
    
    def save_results(self, filename: str):
        """Guarda resultados en JSON"""
        with open(f"results_{self.name}.json", "w") as f:
            json.dump(self.results, f, indent=2)
    
    def add_result(self, result: dict):
        """Agrega un resultado"""
        self.results.append({**result, "timestamp": self.timestamp})
