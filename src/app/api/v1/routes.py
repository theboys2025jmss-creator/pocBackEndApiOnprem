from fastapi import APIRouter, HTTPException

from ...core.config import settings
from ...core.version import getVersion
from ...models.schemas import (
    Echo,
    LoginRequest,
    LoginResponse,
    Order,
    OrderResponse,
    SlowResponse,
    UnstableResponse,
)
from ...services.csv_service import csvService
from ...services.health_service import health
from ...services.simulation_service import simulationService

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


@router.get("/orders", response_model=list[OrderResponse])
def getOrders():
    """Get all orders from CSV file."""

    return csvService.getOrders()


@router.post("/orders", response_model=OrderResponse)
def createOrder(order: Order):
    """Create new order and save to CSV file."""

    return csvService.addOrder(order)


@router.get("/unstable", response_model=UnstableResponse)
async def unstableEndpoint():
    """Simulate unstable endpoint with random failures."""

    return await simulationService.unstableEndpoint()


@router.get("/slow", response_model=SlowResponse)
async def slowEndpoint():
    """Simulate slow endpoint with configurable delay."""

    return await simulationService.slowEndpoint()
