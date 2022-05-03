#função que identifica se o numero passado é multiplo, apenas de 5, 7, dos dois ao mesmo tempo (5,7) ou se não é multiplo
def mutiplos(numero):

    if (numero % 5 == 0) and (numero % 7 == 0):
        print("fizzbuzz")
    elif numero % 5 == 0:
        print("fizz")
    elif numero % 7 == 0:
        print("buzz")
    else:
        print("miss")