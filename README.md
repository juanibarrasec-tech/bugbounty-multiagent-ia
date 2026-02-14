# 🎯 BugBounty Multi-Agent IA

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/juanibarrasec-tech/bugbounty-multiagent-ia)](https://github.com/juanibarrasec-tech/bugbounty-multiagent-ia)

Un **sistema multi-agente IA de código abierto** para automatizar la detección de vulnerabilidades en programas de Bug Bounty. Integra potentes herramientas de pentesting, análisis de IA (OpenAI/Claude), notificaciones en tiempo real y soporte para HackerOne y Bugcrowd.

## ✨ Características

- 🤖 **Multi-Agente IA**: Agentes especializados (escaneo, fuzzing, SQLi, análisis)
- 🧠 **IA Avanzada**: Integración con OpenAI GPT y Anthropic Claude
- 📊 **Dashboards**: Terminal interactiva + Web responsive
- 🔔 **Notificaciones**: Telegram, Discord, Email en tiempo real
- 💾 **Base de Datos**: SQLite con histórico completo de hallazgos
- 🔗 **Integraciones**: HackerOne, Bugcrowd (API integradas)
- 📱 **Termux Compatible**: Funciona en Android con Termux
- 🔧 **Modular y Extensible**: Fácil de agregar nuevos agentes

## 🚀 Quick Start

### Requisitos
- Python 3.8+
- pip
- Git

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/juanibarrasec-tech/bugbounty-multiagent-ia.git
cd bugbounty-multiagent-ia

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
nano .env  # Editar con tus credenciales
```

### Uso Básico

```bash
# Ejecutar sistema principal
python src/bugbounty_ia/main.py

# Dashboard CLI
python -m bugbounty_ia.dashboard.cli_dashboard

# Dashboard Web
python -m bugbounty_ia.dashboard.web_dashboard
```

## 📚 Documentación

- [⚙️ Configuración](docs/configuration.md)
- [🔍 Agentes](docs/agents.md)
- [💾 Base de Datos](docs/database.md)
- [🔔 Notificaciones](docs/notifications.md)
- [📊 Dashboard](docs/dashboard.md)
- [🔗 Integraciones](docs/integrations.md)

## 🎯 Agentes Disponibles

| Agente | Descripción |
|--------|-------------|
| **ScanningAgent** | Escaneo de puertos y servicios con nmap |
| **FuzzingAgent** | Descubrimiento de directorios y paths |
| **SQLiAgent** | Detección de SQL Injection |
| **AIAnalysisAgent** | Análisis inteligente con IA |

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles.

## ⚖️ Disclaimer

Este software es **solo para fines educativos y de investigación**. Solo úsalo en sistemas que tengas permiso explícito para testear.

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para detalles.

## 👤 Autor

**Juan Ibarra** - [@juanibarrasec-tech](https://github.com/juanibarrasec-tech)

---

⭐ Si te gustó este proyecto, ¡dale una estrella en GitHub!
