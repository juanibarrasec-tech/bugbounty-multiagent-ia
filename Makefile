.PHONY: help install install-dev test lint format clean run

help:
	@echo "Comandos disponibles:"
	@echo "  make install      - Instalar dependencias"
	@echo "  make install-dev  - Instalar + dev tools"
	@echo "  make test         - Ejecutar tests"
	@echo "  make lint         - Verificar código"
	@echo "  make format       - Formatear código"
	@echo "  make clean        - Limpiar archivos temporales"
	@echo "  make run          - Ejecutar aplicación"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install black flake8 pylint pytest pytest-cov

test:
	pytest tests/ -v --cov=src

lint:
	flake8 src/
	pylint src/

format:
	black src/ tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache/ .coverage htmlcov/

run:
	python src/bugbounty_ia/main.py

dev-setup: install-dev
	@echo "✅ Entorno de desarrollo configurado"
