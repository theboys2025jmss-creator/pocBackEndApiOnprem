from pydantic import BaseModel


class Echo(BaseModel):
    """Echo message schema."""

    MSG: str
