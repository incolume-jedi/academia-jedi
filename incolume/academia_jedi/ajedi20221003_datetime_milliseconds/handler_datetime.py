from datetime import datetime


def run():
    print(
        "Formatar datetime (local time) em string com "
        "milissegundos (2022-10-03 11:41:07.916)",
        datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        datetime.now().isoformat(sep=' ', timespec='milliseconds'),
        datetime.now().strftime('%F %T.%f')[:-3],
        sep='\n',
        end='\n\n'
    )
    print(
        "Formatar datetime (UTC) em string com "
        "milissegundos (2022-10-03 11:41:07.916)",
        datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        datetime.utcnow().isoformat(sep=' ', timespec='milliseconds'),
        datetime.utcnow().strftime('%F %T.%f')[:-3],
        sep='\n',
        end='\n\n'
    )
    print(
        datetime.now().strftime('%%'),
        sep='\n'
    )


if __name__ == '__main__':    # pragma: no cover
    run()
