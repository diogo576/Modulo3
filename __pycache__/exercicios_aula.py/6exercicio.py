#a função recebe dois nº e devolve o maior e se forem iguais devolve none 
def maiordedois(n1,n2):
    if n1 < n2:
        return n2 #devolver o maior nº
    if n1 > n2:
        return n1
    if n1 == n2:
        return None 
    

    
#print(maiordedois(2,4)) 

assert maiordedois(4,2) == 4,"A função devia devolver 10"
assert maiordedois(2,2) == None,"a função devia devolver none porque os nº são iguais"
print(" A função passou a todos os testes")