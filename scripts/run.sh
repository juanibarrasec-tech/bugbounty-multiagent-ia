#!/bin/bash

echo "🚀 Ejecutando BugBounty IA..."

if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

python src/bugbounty_ia/main.py
