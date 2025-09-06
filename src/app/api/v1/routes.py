from fastapi import APIRouter, HTTPException

from ...core.version import getVersion
from ...models.schemas import Echo
from ...services.health_service import health

router = APIRouter()


@router.get("/health")
def healthz():
    """Health check endpoint."""

    return health()


@router.get("/version")
def version():
    """Get application version information."""

    return getVersion()


@router.post("/echo")
def echo(payload: Echo):
    """Echo back the provided message."""

    if not payload.MSG:
        raise HTTPException(status_code=400, detail="msg required")
    return {"echo": payload.MSG}
