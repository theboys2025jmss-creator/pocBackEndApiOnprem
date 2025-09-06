import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

HEADER = "X-Request-ID"


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Middleware to add request ID to HTTP headers."""

    def __init__(self, app):
        """Initialize the middleware."""

        super().__init__(app)

    async def dispatch(self, request: Request, callNext):
        """Add request ID to request and response headers."""

        reqId = request.headers.get(HEADER, str(uuid.uuid4()))
        response: Response = await callNext(request)
        response.headers[HEADER] = reqId
        return response
