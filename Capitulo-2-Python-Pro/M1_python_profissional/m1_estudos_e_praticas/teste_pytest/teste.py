import pytest
from calculadora import soma
from calculadora import subtracao
from calculadora import multiplicacao


class TesteCalculadora:
    def setup(self):
        pass


    def teste_soma(self):
        resultado = soma(2, 3)
        resultado2 = soma(5, 8)

        assert resultado == 5
        assert resultado2 > 10


    def teste_subtracao(self):
        resultado = subtracao(2,3)

        assert resultado == -1


    def teste_multiplicacao(self):
        resultado = multiplicacao(1, 2)

        assert resultado == 2


    def teste_divisao(self):
        resultado = divisao(15, 5)

        assert resultado == 3

        assert divisao(3, 0) == 0 
        """with pytest.raises(ZeroDivisionError):
            divisao(3, 0) """
