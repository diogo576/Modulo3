#implementar uma função que verifique se uma string é um palindrome 

def palindrome(palavra) -> bool:

    """
    função que indica se uma palavra é um palindrome 
    parametros:
        palavra:string a testar
    devolve:
        true: se é palindrome 
        false:se não é palindrome
    """    

#converter a palavra para minuscula 
    palavra=palavra.lower()
    palavra_invertida=""
    for posição in range(len(palavra)-1,-1,-1):
        palavra_invertida=palavra_invertida + palavra[posição]
    if palavra==palavra_invertida:
        return True
    return False 

if palindrome("banana") == True:
    print("banana é um palindrome")
else:
    print("banana não é um palimdrome")
