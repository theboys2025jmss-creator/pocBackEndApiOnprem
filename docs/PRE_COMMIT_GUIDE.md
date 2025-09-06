# Guía Pre-Commit

## Pasos antes de hacer push

### 1. Formatear código automáticamente
```bash
make format
```
Esto ejecuta:
- `pdm run ruff check . --fix` - Corrige errores automáticamente
- `pdm run ruff format .` - Aplica formato consistente

### 2. Verificar calidad del código
```bash
make quality
```
Esto ejecuta:
- `pdm run ruff check .` - Verifica estilo y errores
- `pdm run ruff format --check .` - Verifica formato
- `pdm run pylint src` - Análisis de código (naming, estructura)
- `pdm run mypy src` - Verificación de tipos
- `pdm run pytest` - Tests unitarios con cobertura

### 3. Comando completo (recomendado)
```bash
make pre-commit
```
Ejecuta format + quality en secuencia.

## Flujo de trabajo recomendado

```bash
# 1. Hacer cambios en el código
git add .

# 2. Verificar y corregir código
make pre-commit

# 3. Si todo pasa, hacer commit
git commit -m "feat: nueva funcionalidad"

# 4. Push
git push
```

## Solución de problemas comunes

### Errores de Ruff
```bash
# Ver errores específicos
pdm run ruff check .

# Corregir automáticamente
pdm run ruff check . --fix
```

### Errores de Pylint
```bash
# Ver errores de naming/estructura
pdm run pylint src
```
Revisar `CODING_STANDARDS.md` para convenciones.

### Errores de Mypy
```bash
# Ver errores de tipos
pdm run mypy src
```
Agregar type hints donde sea necesario.

### Tests fallando
```bash
# Ejecutar tests con más detalle
pdm run pytest -v
```