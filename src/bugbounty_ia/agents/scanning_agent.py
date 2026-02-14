"""
Agente especializado en escaneo de puertos y servicios
"""
import subprocess
from .base_agent import BaseAgent


class ScanningAgent(BaseAgent):
    """Agente para escaneo de puertos usando nmap"""
    
    def __init__(self):
        super().__init__("ScanningAgent")
    
    def execute(self, target: str):
        """Ejecuta escaneo nmap sobre el objetivo"""
        self.log(f"Iniciando escaneo de {target}...")
        
        try:
            # Escaneo básico de puertos comunes
            result = subprocess.run(
                ["nmap", "-F", target], 
                capture_output=True, 
                text=True, 
                check=True
            )
            
            output = result.stdout
            self.add_result({
                "target": target,
                "scan_type": "fast_scan",
                "raw_output": output,
                "status": "completed"
            })
            
            self.log(f"Escaneo completado para {target}")
            return output
            
        except subprocess.CalledProcessError as e:
            self.log(f"Error durante el escaneo: {e}")
            self.add_result({
                "target": target,
                "error": str(e),
                "status": "failed"
            })
            return None
EOF
