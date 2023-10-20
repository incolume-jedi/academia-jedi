from sys import getsizeof

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ranger = range(1, 11)
listcompreention = [x for x in range(1, 11)]
generator = (x for x in range(1, 11))

if __name__ == '__main__':  # pragma: no cover
    print(
        f"""
        tupla: {getsizeof(tupla)} bytes
        lista: {getsizeof(lista)} bytes
        range: {getsizeof(ranger)} bytes
        list compreention: {getsizeof(listcompreention)}
        gerador: {getsizeof(generator)}
        """
    )
