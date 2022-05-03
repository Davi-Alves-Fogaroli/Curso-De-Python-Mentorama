#pesquisei e não consegui corrigir...
#...ou se quer identificar o erro que o vs code aponta neste tipos import que se segue.
import funcoes as f

a = 'S'

while (a == 'S'):
    """
    Pede entrada de um numero natural, chama a função 'f' e o passa o valor de entrada para ela
    """
    numeros = int(input("\ndigite um numero natural: "))    
    
    f.mutiplos(numeros)

    a = input("Se deseja continuar digite 'S': ").upper()
