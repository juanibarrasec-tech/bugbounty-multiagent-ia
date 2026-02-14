"""
Configuración centralizada del sistema
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ========== APIs IA ==========
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "")

# ========== NOTIFICACIONES ==========
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK", "")
EMAIL_CONFIG = {
    "smtp_server": os.getenv("SMTP_SERVER", "smtp.gmail.com"),
    "smtp_port": int(os.getenv("SMTP_PORT", 587)),
    "sender_email": os.getenv("SENDER_EMAIL", ""),
    "sender_password": os.getenv("SENDER_PASSWORD", ""),
}

# ========== BASE DE DATOS ==========
DATABASE_PATH = os.getenv("DATABASE_PATH", "bugbounty_results.db")

# ========== INTEGRACIONES ==========
HACKERONE_USERNAME = os.getenv("HACKERONE_USERNAME", "")
HACKERONE_API_TOKEN = os.getenv("HACKERONE_API_TOKEN", "")
BUGCROWD_API_TOKEN = os.getenv("BUGCROWD_API_TOKEN", "")

# ========== CONFIGURACIÓN DE ESCANEO ==========
SCAN_TIMEOUT = int(os.getenv("SCAN_TIMEOUT", 30))
MAX_THREADS = int(os.getenv("MAX_THREADS", 5))
WORDLIST_PATH = os.getenv("WORDLIST_PATH", "/usr/share/wordlists/")

# ========== NIVELES DE ALERTA ==========
ALERT_LEVELS = {
    "critical": 5,
    "high": 4,
    "medium": 3,
    "low": 2,
    "info": 1
}

MIN_ALERT_LEVEL = int(os.getenv("MIN_ALERT_LEVEL", 3))
