"""
programa para implementar uma caculadora 
simples utilizando funções
"""
def somar(n1,n2):
    """função que recebe dois nº e mostrar a sua soma"""
    print(n1 + n2)
def subtrair(n1,n2):
    """função que recebe  dois nº e mostrar a sua subtração"""
    print(n1 - n2)
def multiplicar(n1,n2):
    """função que recebe dois nº e mostrar a sua multiplicação"""
    print(n1 * n2)
def dividir(n1,n2):
    """função que recebe dois nº e mostrar a sua multiplicação"""
    print(n1 / n2)

def menu():
    """
    mostrar ao utilizador as operações que a calculadora vai realizar
    """
    operação="o"
    while operação!="5":
        print("A.somar\nB.subtrair\nc.multiplicar\nD.dividir")
        operação=input()
        
    n1=float(input("insira um numero:"))
    n2=float(input("insira outro numero:"))
 
    if operação=="A":
        somar(n1,n2)
    elif operação=="B":
        subtrair (n1,n2)
    elif operação=="C":
        multiplicar(n1,n2)
    elif operação=="D":
        dividir(n1,n2)
        
def main():
   menu()
if __name__=="__main__":
    main()