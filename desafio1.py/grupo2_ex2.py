def miaoroumenor(a,b,c):
    #qual o maior 
    if a > b:
        maior = a 
    else:
        maior = b
    if c > maior:
        maior = c 
    #qual o menor
    if a < b:
        menor = a
    else:
        menor= b
    if c < menor:
        menor = c 
    if a > 0 and b > 0 and c > 0:
        return menor 
    return None 