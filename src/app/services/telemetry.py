import time

from ..core.logging import logger


def timedOp(name: str):
    """Decorator to time operations and log results."""

    def decorator(fn):
        def wrapper(*args, **kwargs):
            t0 = time.time()
            try:
                res = fn(*args, **kwargs)
                ok = True
                return res
            except Exception as e:
                ok = False
                logger.error("op.error", op=name, error=str(e))
                raise
            finally:
                dt = (time.time() - t0) * 1000.0
                logger.info("op.done", op=name, ok=ok, latency_ms=round(dt, 2))

        return wrapper

    return decorator
