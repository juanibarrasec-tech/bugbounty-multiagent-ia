"""
Agente especializado en descubrimiento de directorios y paths (Fuzzing)
"""
import requests
from .base_agent import BaseAgent


class FuzzingAgent(BaseAgent):
    """Agente para fuzzing web"""
    
    def __init__(self):
        super().__init__("FuzzingAgent")
    
    def execute(self, target: str, wordlist: list = None):
        """Ejecuta fuzzing básico sobre una URL"""
        if not target.startswith("http"):
            target = f"http://{target}"
            
        self.log(f"Iniciando fuzzing en {target}...")
        
        # Wordlist por defecto muy básica si no se provee una
        common_paths = wordlist or ["admin", "login", "config", "api", ".env", ".git"]
        found_paths = []
        
        for path in common_paths:
            url = f"{target.rstrip('/')}/{path}"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code != 404:
                    self.log(f"Hallazgo: {url} (Status: {response.status_code})")
                    found_paths.append({
                        "url": url,
                        "status_code": response.status_code
                    })
            except requests.RequestException:
                continue
                
        self.add_result({
            "target": target,
            "found_paths": found_paths,
            "status": "completed"
        })
        
        return found_paths
EOF
