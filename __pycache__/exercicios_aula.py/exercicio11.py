#programa que determine o quadrado de um número inteiro 
#o número deve ser pedido ao utilizador, através de uma função 
#devolver o seu quadrado

import math 
#ler um número através de uma função 
def função_quadrado(n:int)->int:
    return n ** 2

def main():
    n = int(input("qual o numero:"))
    q= função_quadrado(n)
    print(f"o quadrado de {n} é {q}")

if __name__=="__main__": 
    main()

    