#uma função que caucula a tabuada de um numero que lhe é passado 
"""
parametros:
n:nº inteiro
output:
    tabuada de 1 a 10 do n 
"""
def tabuada(n):
    for i in range(1,11):
        r=i * n 
        print(f"{i} x {n}= {r}")

tabuada(5)

