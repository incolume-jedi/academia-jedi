import secrets
from typing import Final

from icecream import ic

tries: Final[int] = 3
number: int = secrets.randbelow(3)

for _ in range(tries):
    if (
        my_num := int(input('Dê um palpite e tente adivinhar o número: '))
    ) == number:
        ic(my_num, number)
        print('parabéns você acertou!!!')
        break
    elif my_num < number:
        ic(my_num, number)
        print('O número é maior que o palpite')
    elif my_num > number:
        ic(my_num, number)
        print('O número é menor que o palpite')
