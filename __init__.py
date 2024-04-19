from datetime import datetime
from .logs import getLogger, getWriter


def getName(prefix: str):
    return prefix + datetime.now().strftime("%Y%m%d-%H%M%S")

__all__ = ["getName", getLogger, getWriter]