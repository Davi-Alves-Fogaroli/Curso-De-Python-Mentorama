def fibonacci():
    menu = 'S'

    # while para não ter que reezecutar o codigo toda vez que quiser checar uma nova extenção da sequencia de Fibonacci 
    while menu == 'S':
        # Pede um numero para mostrar n termos da sequencia de Fibonacci

        numero_de_termos = (int(input("\nInsira um numero natural positivo e diferente de zero, correspondente a quantos numeros da se quencia de Fobonacci deseja ver deseja ver: "))) 

        # Os dois primeiros termos da sequencia (imutaveis)

        numero1 = 0
        numero2 = 1
        contador = 0

        # "if" usado para checar se o numero inserio é valido
        if numero_de_termos <= 0 :
            print("Digite um numero valido (Natural positivo e diferente de zero)")
        
        # "elif" usado para otimizar o processo de devolução caso o valor inserido seja 1
        elif numero_de_termos == 1 :
            print(f"Sequencia de Fibonacci até {numero_de_termos} : {numero1}")

        # "else" gerar sequencia para numero_de_termos
        else :
            print("Sequencia de Fibonacci: ")
            
            while contador < numero_de_termos :    
                print(numero1)
                
                # calcula o proximo valor da sequencia
                proximo_valor = numero1 + numero2
                
                # atualiza os valores
                numero1 = numero2
                numero2 = proximo_valor
                
                contador += 1
        menu = (str(input("\nDseja digitar outro numero ? 'S' , 'N'"))).upper()