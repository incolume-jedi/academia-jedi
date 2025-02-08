import datetime as dt

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
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
