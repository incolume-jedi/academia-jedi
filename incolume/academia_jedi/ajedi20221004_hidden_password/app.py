import logging
from getpass import getpass

logFormat = (
    '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;'
    ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
)
logging.basicConfig(format=logFormat, level=logging.DEBUG)


def auth0():
    user, pwd = input('Enter with your Username: '), input(
        'Enter with your Password: ',
    )
    logging.debug(f'{user=}, {pwd=}')
    return (
        user,
        pwd,
    )


def auth1():
    user, pwd = input('Enter with your Username: '), getpass(
        'Enter with your Password: ',
    )
    logging.debug(f'{user=}, {pwd=}')
    return (
        user,
        pwd,
    )


def encoded_input(message: str) -> str:
    print(message)
    pw = ''
    while True:
        symbol = getch.getch()
        if symbol in ['\r', '\n']:
            break
        print('**', end='', flush=True)
        pw += symbol
    print()
    return pw


def auth2():
    user, pwd = input('Enter with your Username: '), encoded_input(
        'Enter with your Password: ',
    )
    logging.debug(f'{user=}, {pwd=}')
    return (
        user,
        pwd,
    )


def run():
    auth0()
    print()
    auth1()


if __name__ == '__main__':
    run()
