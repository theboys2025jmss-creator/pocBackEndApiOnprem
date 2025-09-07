# api-onprem

API FastAPI dockerizada para demos **on-prem**. Estructura lista para crecer:
- core de **config** y **logging** (structlog JSON)
- middlewares (Request ID)
- módulos (rutas v1, servicios, modelos)
- PDM + Makefile + CI/CD (GitHub Actions)

## Desarrollo rápido
```bash
cp .env.example .env
pdm install -G dev
pdm run dev
# http://localhost:8000/docs
```

## Calidad de código

### Antes de hacer commit
```bash
make pre-commit  # Formatea y verifica todo
```

### Comandos individuales
```bash
make format   # Solo formatear
make quality  # Solo verificar
```

## Documentación

- [📋 Guía Pre-Commit](docs/PRE_COMMIT_GUIDE.md) - Pasos antes del push
- [🔍 Guía de Linting](docs/LINTING_GUIDE.md) - Herramientas y configuración
- [📝 Estándares de Código](CODING_STANDARDS.md) - Convenciones de naming
