# syntax=docker/dockerfile:1
FROM python:3.11-slim AS builder
WORKDIR /build

RUN pip install --no-cache-dir pdm==2.19.3
COPY pyproject.toml pdm.lock /build/
RUN pdm export -o requirements.txt --prod --without-hashes

FROM python:3.11-slim AS runtime
WORKDIR /app

COPY --from=builder /build/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
RUN mkdir -p /app/data

EXPOSE 8000
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
