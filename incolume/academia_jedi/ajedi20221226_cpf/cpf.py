import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import re

import rstr

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def validator(cpf: str) -> bool:
    cpf = re.sub(r'.-', '', cpf)
    return cpf_vericator(cpf[:9]) == cpf


def cpf_vericator(cpf: str, is_formated: bool = False) -> str:
    """123.456.789.xy
    x = (1*10 + 2*9 + 3*8 + .. +9*2) * 10 % 11 ¬ Se x == 10 => 0
    y = (1*11 + 2*10 + 3*9 + .. + x*2) * 10 % 11 ¬ Se y == 10 => 0.
    """
    if len(cpf) != 9:
        msg = 'Deve conter exatamente 9 caracteres.'
        raise ValueError(msg)
    if all(cpf[0] == char for char in cpf):
        msg = 'Os Números não dever ser todos iguais.'
        raise ValueError(msg)
    if all(not char.isdigit() for char in cpf):
        msg = 'Informe apenas números'
        raise ValueError(msg)
    for x in (10, 11):
        dig_verif = (
            sum([int(cpf[x - y]) * y for y in range(x, 1, -1)]) * 10 % 11 % 10
        )
        cpf += str(dig_verif)

    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}' if is_formated else cpf


def run():
    regex = r'\d{9}'  # r'\d{3}\.\d{3}\.\d{3}'
    lcpf1 = [rstr.xeger(regex) for _ in range(10)]
    lcpf2 = (f'00000000{x}' for x in range(1, 10))
    try:
        logging.debug(cpf_vericator('794344791'))
    except ValueError as e:
        logging.exception(e)
    print(lcpf1)
    print([cpf_vericator(cpf, True) for cpf in lcpf1])
    print(validator('12345678909'))
    print([cpf_vericator(cpf, True) for cpf in lcpf2])


if __name__ == '__main__':  # pragma: no cover
    run()
