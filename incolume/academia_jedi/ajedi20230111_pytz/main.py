import datetime as dt

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import pytz


def ex01():
    """Exemplo 1."""
    data = dt.datetime.now()
    print(pytz.timezone('America/Sao_Paulo').localize(data))


def ex02():
    """Exemplo 2."""
    data = dt.datetime.strptime('15/6/2021 23:42:21', '%d/%m/%Y %H:%M:%S')
    print(pytz.timezone('America/Sao_Paulo').localize(data))


def ex03():
    """Exemplo 3."""
    a = dt.datetime(2002, 10, 27, 12, 0, 0, tzinfo=pytz.utc).isoformat()
    print(a)


def ex04():
    """Exemplo 4."""
    a = dt.datetime(
        2002,
        10,
        27,
        12,
        0,
        0,
        tzinfo=pytz.timezone('America/Sao_Paulo'),
    ).isoformat()
    print(a)


def ex05():
    """Exemplo 5."""
    data = dt.datetime.strptime('15/6/2021 23:42:21', '%d/%m/%Y %H:%M:%S')
    print(pytz.timezone('America/Sao_Paulo').localize(data).isoformat())


def ex06():
    """Exemplo 5."""
    utc_now = pytz.utc.localize(dt.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone('America/Los_Angeles'))

    print(
        '<',
        pst_now == utc_now,
        '> <',
        utc_now.isoformat(),
        '> <',
        pst_now.isoformat(),
        '>',
    )


def run():
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()
    ex06()


if __name__ == '__main__':
    run()
