"""Estudo datetime."""

import datetime as dt
import logging

import pytz

__author__ = '@britodfbr'  # pragma: no cover


def iso8601_format_01(date: dt.datetime) -> str:
    """Prospecção iso8601 format."""
    result = date.isoformat()
    logging.debug(result)
    return result


def iso8601_format_02() -> str:
    """Prospecção iso8601 format."""
    result = dt.datetime.now(tz=pytz.timezone('UTC')).isoformat(
        sep=' ',
        timespec='milliseconds',
    )
    logging.debug(result)
    return result


def iso8601_format_03(date: dt.datetime) -> str:
    """Prospecção iso8601 format."""
    result = date.isoformat(sep='T', timespec='milliseconds')
    logging.debug(result)
    return result


def iso8601_format_04(date: dt.datetime) -> str:
    """Prospecção iso8601 format."""
    result = date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    logging.debug(result)
    return result


def iso8601_format_05(date: dt.datetime) -> str:
    """Prospecção iso8601 format."""
    result = date.strftime('%F %T.%f%z')
    logging.debug(result)
    return result


def iso8601_format_06(date: dt.datetime) -> str:
    """Prospecção iso8601 format."""
    result = date.isoformat(timespec='milliseconds')
    logging.debug(result)
    return result


def iso8601_format_07(date: dt.datetime) -> str:
    """Prospecção iso8601 format."""
    result = date.replace(microsecond=0).isoformat()
    logging.debug(result)
    return result
