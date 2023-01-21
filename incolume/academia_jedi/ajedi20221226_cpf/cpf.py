import rstr
import logging
import re


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)


def validator(cpf: str) -> bool:
    cpf = re.sub(r".-", "", cpf)
    result = cpf_vericator(cpf[:9]) == cpf
    return result


def cpf_vericator(cpf: str, is_formated: bool = False) -> str:
    """
    123.456.789.xy
    x = (1*10 + 2*9 + 3*8 + .. +9*2) * 10 % 11 ¬ Se x == 10 => 0
    y = (1*11 + 2*10 + 3*9 + .. + x*2) * 10 % 11 ¬ Se y == 10 => 0
    """
    result = ""
    if len(cpf) != 9:
        raise ValueError("Deve conter exatamente 9 caracteres.")
    if all(cpf[0] == char for char in cpf):
        raise ValueError("Os Números não dever ser todos iguais.")
    if all(not char.isdigit() for char in cpf):
        raise ValueError("Informe apenas números")
    for x in (10, 11):
        dig_verif = sum([int(cpf[x - y]) * y for y in range(x, 1, -1)]) * 10 % 11 % 10
        # logging.debug('dig_verif: %s', dig_verif)
        cpf += str(dig_verif)

    result = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if is_formated else cpf
    return result


def run():
    regex = r"\d{9}"  # r'\d{3}\.\d{3}\.\d{3}'
    lcpf1 = [rstr.xeger(regex) for _ in range(10)]
    lcpf2 = (f"00000000{x}" for x in range(1, 10))
    try:
        logging.debug(cpf_vericator("794344791"))
    except ValueError as e:
        logging.error(e)
    print(lcpf1)
    print(list(cpf_vericator(cpf, True) for cpf in lcpf1))
    print(validator("12345678909"))
    print(list(cpf_vericator(cpf, True) for cpf in lcpf2))


if __name__ == "__main__":  # pragma: no cover
    run()
    ...
