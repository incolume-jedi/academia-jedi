"""Academia epoch com python."""
from datetime import datetime


def gerador_epoch(data: datetime, tz: str | None = None) -> int:
    """Gerar epoch."""
    return int(data.strftime('%s', tz))


def reverter_epoch(epoch: int, tz: str | None = None) -> datetime:
    """Reverter epoch para datetime."""
    return datetime.fromtimestamp(epoch, tz)
