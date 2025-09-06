import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .api.v1.routes import router as v1_router
from .core.config import settings
from .core.logging import configureLogging, logger
from .middleware.request_id import RequestIDMiddleware

configureLogging()

app = FastAPI(title="On-Prem Demo API", version=settings.APP_VERSION)

app.add_middleware(RequestIDMiddleware)
if settings.ENABLE_CORS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.middleware("http")
async def logRequests(request: Request, callNext):
    """Log HTTP requests with timing and request ID."""

    requestId = request.headers.get("X-Request-ID", "unknown")
    startTime = time.time()

    logger.info("request.start", requestId=requestId, method=request.method, path=request.url.path)

    resp = await callNext(request)

    duration = round((time.time() - startTime) * 1000, 2)

    logger.info(
        "request.end",
        requestId=requestId,
        method=request.method,
        path=request.url.path,
        status=resp.status_code,
        durationMs=duration,
    )

    return resp


app.include_router(v1_router, prefix="/v1")
