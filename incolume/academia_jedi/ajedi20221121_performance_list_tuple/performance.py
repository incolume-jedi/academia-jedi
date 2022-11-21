from sys import getsizeof


tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == '__main__':    # pragma: no cover
    print(
        f"""
        tupla: {getsizeof(tupla)} bytes
        lista: {getsizeof(lista)} bytes
        """
    )
