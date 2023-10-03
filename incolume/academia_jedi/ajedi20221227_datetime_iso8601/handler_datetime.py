import datetime as dt
import logging


__author__ = '@britodfbr'  # pragma: no cover


def iso8601_format_01(date: dt.datetime):
    result = date.isoformat()
    logging.debug(result)
    return result


def iso8601_format_02():
    result = dt.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
    logging.debug(result)
    return result


def iso8601_format_03(date: dt.datetime):
    result = date.isoformat(sep='T', timespec='milliseconds')
    logging.debug(result)
    return result


def iso8601_format_04(date: dt.datetime):
    result = date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    logging.debug(result)
    return result


def iso8601_format_05(date: dt.datetime):
    result = date.strftime('%F %T.%f%z')
    logging.debug(result)
    return result


def iso8601_format_06(date: dt.datetime):
    result = date.isoformat(timespec='milliseconds')
    logging.debug(result)
    return result


def iso8601_format_07(date: dt.datetime):
    result = date.replace(microsecond=0).isoformat()
    logging.debug(result)
    return result
