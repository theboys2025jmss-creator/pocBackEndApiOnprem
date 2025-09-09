import asyncio
import random
from datetime import datetime

from fastapi import HTTPException

from ..core.config import settings
from ..core.logging import logger
from ..models.schemas import SlowResponse, UnstableResponse


class SimulationService:
    """Service for simulating failures and delays."""

    def __init__(self):
        """Initialize simulation service."""

    async def unstableEndpoint(self) -> UnstableResponse:
        """Simulate unstable endpoint with random failures."""

        timestamp = datetime.now().isoformat()

        if random.choice([True, False]):
            logger.info("unstable.success", timestamp=timestamp)
            return UnstableResponse(
                STATUS="success", MESSAGE="Operation completed successfully", TIMESTAMP=timestamp
            )

        logger.error("unstable.failure", timestamp=timestamp)
        raise HTTPException(status_code=500, detail="Simulated internal server error")

    async def slowEndpoint(self) -> SlowResponse:
        """Simulate slow endpoint with configurable delay."""

        delaySeconds = settings.SLOW_DELAY
        timestamp = datetime.now().isoformat()

        logger.info("slow.start", delay=delaySeconds, timestamp=timestamp)
        await asyncio.sleep(delaySeconds)

        response = SlowResponse(
            MESSAGE=f"Response after {delaySeconds} seconds delay",
            DELAY_SECONDS=delaySeconds,
            TIMESTAMP=timestamp,
        )

        logger.info("slow.complete", delay=delaySeconds, timestamp=timestamp)
        return response


simulationService = SimulationService()
