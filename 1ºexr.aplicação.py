"""
cauculadora para implementar uma caculadora 
simples utilizando funções
"""
def menu():
    """
    mostra as operações que a calculadora vai realizar
    """
    print("A.somar\nB.subtrair\nc.multiplicar\nd.dividir")
    operação=input()
def main():
   menu()
if __name__=="__main__":
    main()