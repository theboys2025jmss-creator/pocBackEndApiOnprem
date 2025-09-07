#!/usr/bin/env bash
set -euo pipefail
cp -n .env.example .env 2>/dev/null || true
echo "Dev listo. Ejecutá: pdm install -G dev && pdm run dev (http://localhost:8000/docs)"
