# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir! Este documento proporciona directrices y pasos para contribuir.

## Código de Conducta

Sé respetuoso, inclusivo y profesional. No se tolera acoso de ningún tipo.

## ¿Cómo contribuir?

### 1. Fork el repositorio
```bash
git clone https://github.com/tu-usuario/bugbounty-multiagent-ia.git
cd bugbounty-multiagent-ia
```

### 2. Crear rama para tu feature
```bash
git checkout -b feature/mi-feature
# o para bugs:
git checkout -b fix/mi-bug
```

### 3. Realizar cambios
- Sigue PEP 8
- Agrega tests para nuevas funcionalidades
- Documenta tu código

### 4. Ejecutar tests y linting
```bash
make test
make lint
make format
```

### 5. Commit y Push
```bash
git add .
git commit -m "feat: descripción clara de cambios"
git push origin feature/mi-feature
```

### 6. Crear Pull Request
- Describe qué cambios hiciste
- Menciona issues relacionados (#123)
- Adjunta screenshots si es UI

## Estándares de Código

- **Python**: PEP 8
- **Commits**: Conventional commits
- **Docstrings**: Google style
- **Tests**: Mínimo 80% cobertura

---

¡Gracias por ayudar! 🎉
