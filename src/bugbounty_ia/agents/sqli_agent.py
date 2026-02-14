"""
Agente especializado en detección de SQL Injection
"""
import requests
from .base_agent import BaseAgent


class SQLiAgent(BaseAgent):
    """Agente para detección de SQLi básica"""
    
    def __init__(self):
        super().__init__("SQLiAgent")
        self.payloads = ["'", "\"", "';--", "admin'--", "' OR 1=1--"]
    
    def execute(self, target_url: str, params: list = None):
        """Prueba payloads de SQLi en parámetros URL"""
        if not target_url.startswith("http"):
            target_url = f"http://{target_url}"
            
        self.log(f"Analizando posibles vulnerabilidades SQLi en {target_url}...")
        
        vulnerabilities = []
        params = params or ["id", "user", "query"]
        
        for param in params:
            for payload in self.payloads:
                test_url = f"{target_url}?{param}={payload}"
                try:
                    response = requests.get(test_url, timeout=5)
                    # Detección simplista basada en errores comunes de SQL
                    sql_errors = ["sql syntax", "mysql_fetch", "sqlite3.error", "psycopg2.error"]
                    if any(error in response.text.lower() for error in sql_errors):
                        self.log(f"¡Posible SQLi detectada en {param} con payload {payload}!")
                        vulnerabilities.append({
                            "param": param,
                            "payload": payload,
                            "url": test_url
                        })
                except requests.RequestException:
                    continue
                    
        self.add_result({
            "target": target_url,
            "vulnerabilities": vulnerabilities,
            "status": "completed"
        })
        
        return vulnerabilities
EOF
