from time import sleep, perf_counter

# exemplo sincrono
st = perf_counter()
print(1)
sleep(1)
print(2)
sleep(1)
print(3)
print("Tempo de execução: {:2.6f}s".format(perf_counter()-st))
