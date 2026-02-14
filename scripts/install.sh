#!/bin/bash

set -e

echo "🚀 Instalando BugBounty IA Multi-Agent System..."

# Detectar OS
if [[ "$OSTYPE" == "linux-android" ]]; then
    echo "📱 Detectado Termux"
    pkg update -y && pkg upgrade -y
    pkg install python git nmap curl -y
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Detectado Linux"
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip git nmap curl
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 Detectado macOS"
    brew install python nmap curl
fi

# Crear venv
python -m venv venv
source venv/bin/activate

# Instalar deps
pip install --upgrade pip
pip install -r requirements.txt

# Copiar .env
cp .env.example .env

echo "✅ ¡Instalación completada!"
echo ""
echo "📝 Próximos pasos:"
echo "1. Edita .env con tus credenciales"
echo "2. source venv/bin/activate"
echo "3. python src/bugbounty_ia/main.py"
