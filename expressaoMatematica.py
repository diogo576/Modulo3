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
    contar = 0
    for l in expressao:
        if l == "(":
            contar = contar + 1
        if l ==")":
            contar = contar - 1
        if contar < 0 :
            return False 
    if contar == 0:
        return True 
    return False 


#chamar a função 
resultado = validar(expressao)

#indicar ao utilizador se a expressão é ou nao valida
if resultado == False:
    print("A expressao nao é valida")
else:
    print("a expressao é valida")