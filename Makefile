REGISTRY ?= ghcr.io/TU-ORG
IMAGE    ?= api-onprem
TAG      ?= 1.0.0

# Formateo automático de código
format:
	pdm run ruff check . --fix
	pdm run ruff format .

# Verificación de calidad completa
quality:
	pdm run ruff check .
	pdm run ruff format --check .
	pdm run pylint src
	pdm run mypy src
	pdm run pytest -q --maxfail=1 --disable-warnings --cov=src --cov-report=term-missing

# Preparar código antes del commit
pre-commit: format quality
	@echo "✅ Código listo para commit"

# Docker build
build:
	docker build -t $(REGISTRY)/$(IMAGE):$(TAG) .

# Docker push
push:
	docker push $(REGISTRY)/$(IMAGE):$(TAG)
