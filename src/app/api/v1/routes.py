from typing import List

from fastapi import APIRouter, HTTPException

from ...core.version import getVersion
from ...models.schemas import Echo, Order, OrderResponse, SlowResponse, UnstableResponse
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


@router.get("/orders", response_model=List[OrderResponse])
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
