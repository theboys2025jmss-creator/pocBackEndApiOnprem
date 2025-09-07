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
    """Log HTTP requests start and end."""

    logger.info("request.start", method=request.method, path=request.url.path)
    resp = await callNext(request)
    logger.info("request.end", status=resp.status_code)
    return resp


app.include_router(v1_router, prefix="/v1")
