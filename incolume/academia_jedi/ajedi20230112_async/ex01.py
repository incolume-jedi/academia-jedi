from time import perf_counter, sleep

# exemplo sincrono
st = perf_counter()
print(1)
sleep(1)
print(2)
sleep(1)
print(3)
print(f'Tempo de execução: {perf_counter() - st:2.6f}s')
