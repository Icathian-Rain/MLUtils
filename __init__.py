from datetime import datetime
from .logs import getLogger, getWriter, Logs
from .acc import AverageMeter


def getName(prefix: str):
    return prefix + datetime.now().strftime("%Y%m%d-%H%M%S")

__all__ = ["getName", getLogger, getWriter, Logs, AverageMeter]