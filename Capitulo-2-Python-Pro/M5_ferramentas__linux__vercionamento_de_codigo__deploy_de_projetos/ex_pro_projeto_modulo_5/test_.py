#testes para validar a função: "def mutiplos(numero):", do arquivo: "funcoes.py"

import pytest
import funcoes as f
    
class TestMultiplos:
    def setup(self):
        pass

    def test_multiplos_sete_cinco(self):
        resultado1 = f.mutiplos(35)
        assert resultado1 == "fizzbuzz"

    def test_multiplos_cinco(self):
        resultado2 = f.mutiplos(5)
        assert resultado2 == "fizz"

    def test_multiplos_sete(self):
        resultado3 = f.mutiplos(7)
        assert resultado3 == "buzz"

    def test_nao_multiplo(self):
        resultado4 = f.mutiplos(3)
        assert resultado4 == "miss"
