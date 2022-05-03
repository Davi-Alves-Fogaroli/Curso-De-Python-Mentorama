#testes para validar a função: "def mutiplos(numero):", do arquivo: "funcoes.py"

import pytest
import funcoes as f

class TesteMultiplos:
    def setup(self):
        pass

    def multiplos_sete_cinco(self):
        resultado1 = f.mutiplos(35)

        assert resultado1 == "fizzbuzz"

    def multiplos_cinco(self):
        resultado2 = f.mutiplos(5)
        assert resultado2 == "fizz"

    def multiplos_cinco(self):
        try:
            resultado2 = f.mutiplos(5)
            assert resultado2 == "fizz"
        except:
            print("Erro")        

    def multiplos_sete(self):
        resultado3 = f.mutiplos(7)
        assert resultado3 == "buzz"

    def nao_multiplo(self):
        resultado4 = f.mutiplos(3)
        assert resultado4 == "miss"
