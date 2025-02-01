# programa para ler do utilizador uma string e indica se a expressão está correta ou não 
# verificar se os parenteses estão corretamente ligados entre si, ou seja:"()"ou "(())"

#pedir ao utilizador a expressão
expressao = input("introduza uma expressão")

#fazer a validação  com uma função
def validar(expressao):
    """
    função que recebe uma expressão matematica para validar os ()
    A função devolve False de a expressao tiver erros de outra forma devolve True 
    """
    abriu=""
    for l in expressao:
        if l == "(" or l=="[":
            abriu = abriu + l
        if l ==")" or l =="]":
            if abriu =="": 
                return False 
            ultimo =abriu[len(abriu)-1]
            if (ultimo =="(") or (ultimo == "[" and l =="]"):
                temp =abriu
                #limpar a string para copiar todos os caracteres menos o ultimo 
                abriu =""
                for i in range(len(temp)-1):
                    abriu = abriu + temp[i]
            else:
                return False 
          
    if abriu =="":
        return False             
    return False 

#chamar a função 
resultado = validar(expressao)

#indicar ao utilizador se a expressão é ou nao valida
if resultado == False:
    print("A expressao nao é valida")
else:
    print("a expressao é valida")