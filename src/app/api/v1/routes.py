from fastapi import APIRouter, HTTPException

from ...core.config import settings
from ...core.version import getVersion
from ...models.schemas import Echo, LoginRequest, LoginResponse
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


@router.post("/login", response_model=LoginResponse)
def login(credentials: LoginRequest):
    """Basic login endpoint with Admin/root credentials."""

    if credentials.username == settings.ADMIN_USER and credentials.password == settings.ADMIN_PASS:
        return LoginResponse(success=True, message="Login successful", token="demo-token-12345")

    return LoginResponse(success=False, message="Invalid credentials")
