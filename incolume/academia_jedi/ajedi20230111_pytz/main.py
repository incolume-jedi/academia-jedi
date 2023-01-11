import pytz
import datetime as dt


def ex01():
    """Exemplo 1"""
    data = dt.datetime.now()
    print(pytz.timezone("America/Sao_Paulo").localize(data))


def ex02():
    """Exemplo 2"""
    data = dt.datetime.strptime("15/6/2021 23:42:21", "%d/%m/%Y %H:%M:%S")
    print(pytz.timezone("America/Sao_Paulo").localize(data))


def ex03():
    """Exemplo 3"""
    a = dt.datetime(2002, 10, 27, 12, 0, 0, tzinfo=pytz.utc).isoformat()
    print(a)


def ex04():
    """Exemplo 4"""
    a = dt.datetime(2002, 10, 27, 12, 0, 0, tzinfo=pytz.timezone("America/Sao_Paulo")).isoformat()
    print(a)


def ex05():
    """Exemplo 5"""
    data = dt.datetime.strptime("15/6/2021 23:42:21", "%d/%m/%Y %H:%M:%S")
    print(pytz.timezone("America/Sao_Paulo").localize(data).isoformat())
    #print(data.isoformat())


def ex06():
    """Exemplo 5"""
    utc_now = pytz.utc.localize(dt.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))

    print('<',
        pst_now == utc_now, '> <',
        utc_now.isoformat(), '> <',
        pst_now.isoformat(), '>'
    )


def run():
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()
    ex06()


if __name__ == "__main__":
    run()
