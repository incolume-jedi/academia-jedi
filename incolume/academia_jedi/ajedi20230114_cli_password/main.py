import pwinput


def get_pwd(msg: str = ''):
    msg = msg or 'Informe tua senha: '
    return input(msg)


def get_pwd_ofuscated(msg: str = ''):
    msg = msg or 'Informe tua senha: '
    return pwinput.pwinput(msg, mask='*')


def run():
    print(get_pwd())
    print(get_pwd_ofuscated())


if __name__ == '__main__':  # pragma: no cover
    run()
