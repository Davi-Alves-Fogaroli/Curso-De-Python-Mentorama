class Fib1():

    def __init__(self, iteracao):
        self.iteracao = iteracao
        self.anterior = 0
        self.proximo = 1

    # Retorna um objeto que expoem o metodo __next__ ...
    #...self(cujo tipo é fibonacci) é esse o objeto:
    def __iter__(self):
        return self
    
    def __next__(self):
        
        # Nos retornamos o contagem de numero de fibonacci. 
        # "raise StopIteration" Indica o erre que ocorrera ao alcançar o valor delimitado e faz a iteração parar
        if self.iteracao == 0:
            raise StopIteration

        proximovalor = self.anterior + self.proximo            
        self.anterior = self.proximo
        self.proximo = proximovalor

        self.iteracao -= 1

        # O ex, pede pararetornar o proximo, no entanto o anterior, é melhor para...
        #...representar a sequencia de Fibonacci
        return self.proximo

# Passa o a quantidade de numeros de Fibonacci que deseja ver
nums = Fib1(10)

# Mostra os numeros 
print("Sequencia de Fibonacci: ")
for num in nums:
    print(num)

# Chamo o metodo de inicialização diretamente e passo o valor.
nums.__init__(10)
# Quando os valores retrnados, em um dic compreension, onde as chaves são criadas pela função nativa enumerate
dicionario = {k : v for k, v in enumerate(nums)}
print("Dicionario (posição:valor): \n",dicionario,"\n")
