import string
from itertools import pairwise

# pares sem pairwise
for i in range(len(alph := string.ascii_uppercase[:8]) - 1):
    print(alph[i], alph[i + 1])

print()
# aplicação do pairwise
for pair in pairwise(string.ascii_uppercase[:8]):
    print(*pair)
