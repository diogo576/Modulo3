#uma função que recebe um numero e indica se é primo ou nao 

def primo(n) -> bool:
    
    e_primo=True
    for i in range (2,n):
        if n % i == 0:
            e_primo= False 
            break 
    return e_primo 

if primo(5)== True:
    print("o nº 5 é primo")
else :
    print("o nº 5 não é primo")
