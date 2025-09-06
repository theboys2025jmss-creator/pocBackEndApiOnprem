# Guía de Linting

## Herramientas de linting configuradas

### 1. Ruff - Linter rápido y formateador
```bash
# Verificar errores
pdm run ruff check .

# Corregir automáticamente
pdm run ruff check . --fix

# Formatear código
pdm run ruff format .

# Verificar formato sin cambios
pdm run ruff format --check .
```

**Qué verifica:**
- Imports sin usar
- Espacios y saltos de línea
- Longitud de líneas
- Sintaxis y errores básicos

### 2. Pylint - Análisis de código y naming
```bash
pdm run pylint src
```

**Qué verifica:**
- Convenciones de naming (camelCase, PascalCase, UPPER_CASE)
- Estructura de clases y funciones
- Docstrings obligatorios
- Complejidad de código

**Configuración en `.pylintrc`:**
- Variables: `camelCase`
- Funciones: `camelCase` 
- Clases: `PascalCase`
- Constantes: `UPPER_CASE`

### 3. Mypy - Verificación de tipos
```bash
pdm run mypy src
```

**Qué verifica:**
- Type hints correctos
- Compatibilidad de tipos
- Imports de tipos

### 4. Pytest - Tests y cobertura
```bash
pdm run pytest -q --maxfail=1 --disable-warnings --cov=src --cov-report=term-missing
```

**Qué verifica:**
- Tests unitarios pasan
- Cobertura de código
- Funcionalidad correcta

## Comandos Make disponibles

```bash
# Solo formatear
make format

# Solo verificar calidad
make quality  

# Ambos (recomendado antes de commit)
make pre-commit
```

## Configuración de archivos

### `.pylintrc`
- Naming conventions
- Mensajes deshabilitados
- Formato de líneas

### `pyproject.toml`
- Configuración de Ruff
- Configuración de Mypy
- Scripts de PDM

### `Makefile`
- Comandos rápidos
- Flujo de CI/CD

## Integración con IDE

### VS Code
Instalar extensiones:
- Python
- Pylint
- Ruff

### PyCharm
- Configurar Pylint como external tool
- Habilitar Mypy en settings