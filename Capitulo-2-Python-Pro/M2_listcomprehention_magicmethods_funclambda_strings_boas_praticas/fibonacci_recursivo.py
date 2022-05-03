#### OBS: Magia da braba, aprender. XP
def recur_fibo(n):

    if n <= 1:
       return n

    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
# 
# Começo do codigo, inserre quantidade de numeros de fibonacci que deseja ver
#
nterms = 10 #(int(input("""Digite a quantidade de numeros de fibonacci que deseja ver.
          #          OBS: numeros inteiros positivos e diferentes de zero: """)))

# Caso recomeço/validação do valor de entrada
if nterms <= 0:
   print("Insira um positivo inteiro")

# Caso o  
else:
   print("Sequencia de Fibonacci:")

   for i in range(nterms):
       print(recur_fibo(i))