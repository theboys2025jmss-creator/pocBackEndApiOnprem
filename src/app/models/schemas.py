from typing import Optional

from pydantic import BaseModel


class Echo(BaseModel):
    """Echo message schema."""

    MSG: str


class LoginRequest(BaseModel):
    """Login request schema."""

    username: str
    password: str


class LoginResponse(BaseModel):
    """Login response schema."""

    success: bool
    message: str
    token: Optional[str] = None
