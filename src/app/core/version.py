from .config import settings


def getVersion() -> dict:
    """Get application version and environment information."""

    return {
        "service": settings.SERVICE_NAME,
        "version": settings.APP_VERSION,
        "env": settings.APP_ENV,
    }
