# Ejemplo de Uso en Repositorios de Solución

Este archivo muestra cómo usar la imagen `api-onprem` en repositorios de solución.

## Estructura de Repositorio de Solución

```
mi-solucion-aws/
├── datasets/
│   ├── orders.csv
│   ├── products.csv
│   └── customers.csv
├── docker-compose.yml
├── README.md
└── .env
```

## docker-compose.yml

```yaml
version: '3.8'

services:
  api-onprem:
    image: ghcr.io/<org>/api-onprem:latest
    ports:
      - "8000:8000"
    environment:
      - APP_ENV=production
      - LOG_LEVEL=INFO
      - DATA_PATH=/app/data
      - SLOW_DELAY=3
    volumes:
      # Montar datasets específicos de la solución
      - ./datasets/orders.csv:/app/data/orders.csv
      - ./datasets/products.csv:/app/data/products.csv
      - ./datasets/customers.csv:/app/data/customers.csv
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/v1/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Otros servicios de la solución (CloudWatch agent, etc.)
  cloudwatch-agent:
    image: amazon/cloudwatch-agent:latest
    # ... configuración específica
```

## Ejemplo de Dataset (datasets/orders.csv)

```csv
ORDER_ID,CUSTOMER_NAME,PRODUCT,QUANTITY,PRICE,ORDER_DATE
ord-001,Acme Corp,Widget A,100,25.99,2024-01-15T10:30:00
ord-002,Beta Inc,Widget B,50,45.50,2024-01-15T11:45:00
ord-003,Gamma LLC,Widget C,75,35.00,2024-01-15T14:20:00
```

## Comandos

```bash
# Levantar la solución completa
docker-compose up -d

# Ver logs de la API
docker-compose logs -f api-onprem

# Probar endpoints
curl http://localhost:8000/v1/health
curl http://localhost:8000/v1/orders

# Crear nueva orden
curl -X POST http://localhost:8000/v1/orders \
  -H "Content-Type: application/json" \
  -d '{
    "CUSTOMER_NAME": "New Customer",
    "PRODUCT": "New Product",
    "QUANTITY": 1,
    "PRICE": 99.99
  }'
```

## Ventajas de esta Arquitectura

1. **Separación de responsabilidades**: Esqueleto vs datos
2. **Reutilización**: Misma imagen base para múltiples soluciones
3. **Flexibilidad**: Cada solución define sus propios datasets
4. **Versionado independiente**: Esqueleto y datos evolucionan por separado
5. **CI/CD simplificado**: Solo se construye la imagen base una vez