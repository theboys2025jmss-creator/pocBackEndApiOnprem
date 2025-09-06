from typing import Optional

from pydantic import BaseModel, Field


class Echo(BaseModel):
    """Echo message schema."""

    MSG: str


class Order(BaseModel):
    """Order data schema."""

    ORDER_ID: Optional[str] = None
    CUSTOMER_NAME: str = Field(..., min_length=1)
    PRODUCT: str = Field(..., min_length=1)
    QUANTITY: int = Field(..., gt=0)
    PRICE: float = Field(..., gt=0)
    ORDER_DATE: Optional[str] = None


class OrderResponse(BaseModel):
    """Order response schema."""

    ORDER_ID: str
    CUSTOMER_NAME: str
    PRODUCT: str
    QUANTITY: int
    PRICE: float
    ORDER_DATE: str


class UnstableResponse(BaseModel):
    """Unstable endpoint response schema."""

    STATUS: str
    MESSAGE: str
    TIMESTAMP: str


class SlowResponse(BaseModel):
    """Slow endpoint response schema."""

    MESSAGE: str
    DELAY_SECONDS: int
    TIMESTAMP: str
