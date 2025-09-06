
---

### `DEPLOY.md` (si todavía no lo creaste completo)
```md
# Despliegue / Build & Push de imagen

## Prerrequisitos
- Docker, PDM, Python 3.11
- GitHub con acceso a GHCR (o tu registro favorito)

## Build local
```bash
make build TAG=1.0.0 REGISTRY=ghcr.io/TU-ORG
