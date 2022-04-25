
No arquivo "variaveis_estruturas_e_tipos_de_dados.ipynb" se encontra os codigos resposta para os execicios abaixo. 

*Onde foram praticados conseitos tecnicos de:
	-Biblioteca "macth"
	-Estruturas: 
		~ De repetição "while","for"
		~ condicionais "if","elif","else"
	-Operadores logicos (and, or, not)
	-Operadores relacionais (>, <, >=, <=, !=, ==)
	-Operadores matematicos (**, %, -, +, ...)
	-Variaveis type(list, dic, int, str, float)

    1)Faça um programa que imprime seu nome completo na tela

    2)Escreva um programa que exiba o resutado de 5a x 3b onde a=2 e b=5

    3)Modifique o programa anterior, inserindo uma terceira variável c=5 e imprima a soma das três variáveis

    4)Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma(+),...
    ...subtração(-),Multiplicação(*) e divisão(/). Exiba o resultado da operação

    5)Escreva um programa para contar de 1 até 10.

    6)Escreva um programa para contar quantos números pares e ímpares existentes entre 1 e 10 bem como a soma deles
        a)usando a instrução while r=0 par  r=1 inpar
        b)usando a instrução for e as funções rande e sum

    7) Escreva um programa para resolver enquações do segundo grau representadas por ax^2+bx+c usando a Fórmula de Bhaskara
        a) sem usar o módulo matha=float(input("insira o valor da variavel a"))
        b) usando o módulo math

    8)Vamos reescrever o programa acima criando uma função bhaskara que recebe como parâmetros os coeficientes a, b e c e retorna as raizes da equação.
        a)Oq significa palavra reservada em python, quais as palavras reservadas no código dado? 
        b)Qual a função de cada uma dessas palavras reservadasno código?
        c) implemente a função dada e mostre o resultado :
---------------------------------------c---------------------------------------
    def bhaskara(a, b, c):
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return None
        else:
            raizes = []
            m1 = math.sqrt(delta)s
            r1 =(-b +m1) / (2*a)
            raizes.append(r1)
            r2 =(-b +m1) / (2*a)
            raizes.append(r2)
            return raizes
 ---------------------------------------c---------------------------------------
    9)Considerando a string s='Mentorama' escreva um programa que:
        a)converta a string para maiúsculo, em seguida
        b)Imprima-a de trás para frente
        c)imprima somente as vogais

    10)Escreva um programa que receba como entrada do usuario o nome "João" sobrenome "da Silva", idade"25", cidade "São Paulo",... 
    ...ddd"11", telefone"3333-3333" e faça as seguintes instruções:
        a)imprima na tela o nome completo em uma única linha Nome: João da Silva
        b)print telefone com dd Telefone: (11)3333-3333
        c)print idade: 25
        d)print Cidade: São Paulo