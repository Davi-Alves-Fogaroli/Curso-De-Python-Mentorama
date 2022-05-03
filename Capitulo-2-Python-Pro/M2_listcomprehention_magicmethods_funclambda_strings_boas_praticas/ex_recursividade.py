def contador(numero,numero_max):
    if numero != numero_max: 
        print(numero)
        contador(numero+1,numero_max)
contador(2,8)