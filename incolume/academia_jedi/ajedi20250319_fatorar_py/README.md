# Acadêmia JEDI

**[Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW) - Grupo Python Incolume**

**JEDI - Junta Especializada de Desenvolvimento e Inovação**
- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Fatoração de testes unittest para pytest**

Com base no código **unittest** a seguir, implemente uma nova rotina de testes em **pytest**.

```python
"""test_main.py """
import unittest
from dataclasses import is_dataclass
from main import Product

class TestProduct(unittest.TestCase):

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Product))

    def setUp(self):
        self.product = Product(1, 'test', 1.0, 10)

    def test_constructor(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, 'test')
        self.assertEqual(self.product.price, 1.0)
        self.assertEqual(self.product.stock, 10)

    def test_increse_stock(self):
        self.product.increase_stock(10)
        self.assertEqual(self.product.stock, 20)

    def test_decrease_stock(self):
        self.product.decrease_stock(10)
        self.assertEqual(self.product.stock, 0)

if __name__ == "__main__":
    unittest.main()
```

```python
"""Main.py"""
from dataclasses import dataclass

@dataclass()
class Product:

    id: int
    name: str
    price: float
    stock: int

    def increase_stock(self, stock_to_add: int):
        self.check_positive_number(stock_to_add)
        self.stock: int = self.stock + stock_to_add

    def decrease_stock(self, stock_to_reduce):
        self.check_positive_number(stock_to_reduce: int)
        new_stock = self.stock - stock_to_reduce
        self.check_negative_stock(new_stock)
        self.stock = self.stock - stock_to_reduce

    def check_positive_number(self, value):
        if value <= 0:
            raise Exception("Number must be positive")

    def check_negative_stock(self, value):
        if value < 0:
            raise Exception("Stock must be greater than or equal to 0")

```

## Resultado esperado

O que é esperado na conclusão deste ‘sprint’


## Exemplos

<details>
  <summary>Spoiler?</summary>

  **Passos necessários**:

  1. TDD válido;
  1. Cobertura de testes em 100% do código implementado;
  1. Executar e passar em todos os testes: `$ pytest`;
  1. Executar e passar em todos os linters homologados: `$ task lint`;
  1. Executar e passar no lint ruff: `$ task lint_ruff`;
  1. Executar e passar em todos os linters ativos `$ task lint_all`;

   **Considerar em caso de fatoração**:

    > modo pythônico
    > sem condicionais
    > estruturas performáticas
    > redução de complexidade ciclomática
    > análise assintótica de algoritmos (big O)

</details>

N/A - Exemplos de solução e resposta do problema. Geralmente utilizado para validar os testes do TDD.



## Referências

- https://github.com/gabrielcjr/unittest/blob/master
- https://youtu.be/CHi6h87eNbA?si=t1EogVyPc-yPh9_I
 - N/A (Caso haja referências podem ser listadas aqui)


---
Copyright &copy; **incolume.com.br** since 2010
