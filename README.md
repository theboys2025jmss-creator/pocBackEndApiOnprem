# API On-Prem

> **Esqueleto de API FastAPI** para simular backends on-premises. Genera imagen Docker genérica que recibe datasets externos vía volúmenes.

## 🚀 Características

- **FastAPI** con documentación automática (Swagger/OpenAPI)
- **Logging estructurado** con JSON (structlog)
- **Middlewares** personalizados (Request ID, CORS)
- **Arquitectura modular** (core, services, models, routes)
- **Gestión de dependencias** con PDM
- **Calidad de código** automatizada (Ruff, Pylint, Mypy)
- **Tests** unitarios con cobertura
- **CI/CD** con GitHub Actions
- **Docker** multi-stage para producción

## 📁 Estructura del Proyecto

```
pocBackEndApiOnprem/
├── src/app/                    # Código fuente principal
│   ├── api/v1/                # Rutas API versión 1
│   │   └── routes.py          # Endpoints (/health, /version, /echo)
│   ├── core/                  # Configuración y utilidades base
│   │   ├── config.py          # Settings con Pydantic
│   │   ├── logging.py         # Configuración structlog
│   │   └── version.py         # Info de versión
│   ├── middleware/            # Middlewares personalizados
│   │   └── request_id.py      # Request ID tracking
│   ├── models/                # Modelos de datos
│   │   └── schemas.py         # Schemas Pydantic
│   ├── services/              # Lógica de negocio
│   │   ├── health_service.py  # Health checks
│   │   └── telemetry.py       # Métricas y timing
│   ├── utils/                 # Utilidades generales
│   │   └── time.py            # Funciones de tiempo
│   └── main.py                # Aplicación FastAPI principal
├── tests/                     # Tests unitarios
├── docs/                      # Documentación
├── scripts/                   # Scripts de desarrollo
├── .github/workflows/         # CI/CD GitHub Actions
├── Dockerfile                 # Imagen Docker multi-stage
├── pyproject.toml            # Configuración PDM y herramientas
├── Makefile                  # Comandos de desarrollo
└── .env.example              # Variables de entorno ejemplo
```

## 🛠️ Desarrollo del Esqueleto

### Prerrequisitos
- Python 3.11+
- PDM (Python Dependency Manager)
- Docker

### Setup para desarrollo
```bash
# 1. Clonar repositorio
git clone <repo-url>
cd pocBackEndApiOnprem

# 2. Instalar dependencias
pdm install -G dev

# 3. Ejecutar en modo desarrollo (sin datos)
pdm run dev
```

### Verificar esqueleto
- **API**: http://localhost:8000
- **Documentación**: http://localhost:8000/docs
- **Health**: http://localhost:8000/v1/health

### Endpoints disponibles

#### Core
- `GET /v1/health` - Health check
- `GET /v1/version` - Información de versión
- `POST /v1/echo` - Echo de mensajes

#### Datos (CSV)
- `GET /v1/orders` - Obtener todas las órdenes
- `POST /v1/orders` - Crear nueva orden

#### Simulación
- `GET /v1/unstable` - Endpoint inestable (50% falla con 500)
- `GET /v1/slow` - Endpoint lento (delay configurable)

## 🧪 Testing y Calidad

### Comandos rápidos
```bash
# Formatear código automáticamente
make format

# Verificar calidad completa
make quality

# Preparar para commit (format + quality)
make pre-commit
```

### Comandos individuales
```bash
# Linting y formato
pdm run ruff check . --fix
pdm run ruff format .

# Análisis de código
pdm run pylint src
pdm run mypy src

# Tests con cobertura
pdm run pytest -q --cov=src --cov-report=term-missing
```

## 🐳 Docker

### Desarrollo con Docker

#### Construir imagen localmente
```bash
# Construir imagen
docker build -t api-onprem .

# Verificar imagen
docker images | grep api-onprem
```

#### Uso en repositorios de solución
```yaml
# docker-compose.yml en repo de solución
services:
  api-onprem:
    image: ghcr.io/<org>/api-onprem:latest
    ports:
      - "8000:8000"
    volumes:
      - ./datasets/orders.csv:/app/data/orders.csv
      - ./datasets/products.csv:/app/data/products.csv
    environment:
      - APP_ENV=production
      - DATA_PATH=/app/data
```

### Construir y publicar imagen

#### 1. Construir imagen
```bash
# Clonar repositorio esqueleto
git clone <repo-url>
cd pocBackEndApiOnprem

# Construir imagen
docker build -t api-onprem:latest .
```

#### 2. Publicar en registry
```bash
# Tag para registry
docker tag api-onprem:latest ghcr.io/<org>/api-onprem:latest

# Push al registry
docker push ghcr.io/<org>/api-onprem:latest
```

#### 3. Verificar imagen
```bash
# Probar imagen sin datos (solo health check)
docker run --rm -p 8000:8000 api-onprem:latest &
sleep 5
curl http://localhost:8000/v1/health
```

## 🔧 Configuración

### Variables de entorno (.env)
```bash
APP_ENV=dev                    # Entorno (dev/staging/production)
APP_VERSION=1.0.0             # Versión de la aplicación
LOG_LEVEL=INFO                # Nivel de logging
SERVICE_NAME=api-onprem       # Nombre del servicio
HTTP_HOST=0.0.0.0             # Host de binding
HTTP_PORT=8000                # Puerto de la aplicación
ENABLE_CORS=true              # Habilitar CORS
DATA_PATH=/app/data           # Ruta base para datasets CSV
SLOW_DELAY=5                  # Delay en segundos para /slow
```

### Datasets y Persistencia
- **CSV**: Lee archivos CSV montados externamente
- **Volumen**: `/app/data` para recibir datasets desde repositorios de solución
- **Sin datos**: Este repo NO incluye datasets, solo la imagen base
- **Auto-creación**: Directorios se crean automáticamente si no existen

### Simulación de Escenarios
- **Fallos aleatorios**: `/unstable` para probar resiliencia
- **Latencia**: `/slow` para probar timeouts y escalado
- **Observabilidad**: Logs estructurados con timing y request ID

### Logging
- **Formato**: JSON estructurado
- **Campos**: timestamp, level, message, context, requestId, durationMs
- **Request tracking**: X-Request-ID automático
- **Telemetría**: Timing de operaciones y errores simulados

## 🚀 CI/CD

El pipeline de GitHub Actions:
1. **Lint & Test**: Verifica calidad y ejecuta tests
2. **Build**: Construye imagen Docker
3. **Push**: Sube imagen al registry (GHCR)
4. **Deploy**: Despliega automáticamente (si configurado)

## 🎯 Casos de Uso

### Simulación de Sistemas On-Premise
- **Datos**: Servir datasets desde CSV como si fuera un ERP/CRM legacy
- **Fallos**: Simular inestabilidad de sistemas antiguos
- **Latencia**: Probar comportamiento con sistemas lentos

### Testing de Soluciones AWS
- **CloudWatch**: Monitorear logs estructurados y métricas
- **Auto Scaling**: Probar escalado con endpoints lentos
- **SQS/SNS**: Manejar fallos con colas y notificaciones
- **Lambda**: Procesar eventos de la API

### Esqueleto para Repositorios de Solución
- **Imagen base**: Repositorios de solución usan `ghcr.io/<org>/api-onprem:latest`
- **Datasets externos**: Cada solución monta sus propios CSV/Parquet
- **Configuración flexible**: Variables de entorno para personalizar comportamiento
- **Sin acoplamiento**: Separación clara entre esqueleto y datos

## 📚 Documentación

- [📋 Guía Pre-Commit](docs/PRE_COMMIT_GUIDE.md) - Pasos antes del push
- [🔍 Guía de Linting](docs/LINTING_GUIDE.md) - Herramientas y configuración
- [📝 Estándares de Código](CODING_STANDARDS.md) - Convenciones de naming
- [📜 Ejemplo de Uso](USAGE_EXAMPLE.md) - Cómo usar en repositorios de solución

## 🤝 Contribuir

1. Fork del repositorio
2. Crear branch: `git checkout -b feature/nueva-funcionalidad`
3. Hacer cambios y ejecutar: `make pre-commit`
4. Commit: `git commit -m 'feat: nueva funcionalidad'`
5. Push: `git push origin feature/nueva-funcionalidad`
6. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT.
