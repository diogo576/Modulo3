"""
implemente um programa que codifica ou descodifica uma mensagem com base nos alfabetos fornecidos
"""
original = "abcdefghijklmnopqrstuvxyz"
codigo = "bcdefghijklmnopqrstuvxyza"

def menu():
    """função para ler a opção do utilizador e executar a função adequada:codificar ou descodificar"""
pass

def codificar(mensagem:str)->str:
    """
    função que recebe uma mensagem e devolve a mesma codificada de acordo com os alfabetos fornecidos 
    """
    global original
    global codigo
    texto=" "
    for L in mensagem:
        if L not in original:
            texto= texto + L
        else:
            for P in range(len(original)):
                if L == original[P]:
                    texto == texto + codigo[P]
        

        #caso nao encontre a letra no alfabeto deve manter a variavel original 
    return texto 
def descodificar(mensagem_codificada:str)-> str:
    """
    funçao que recebe uma mensagem codificada e devolve a mesma descodificada de acordo com os alfabetos fornecidos 
    """
    for L in mensagem_codificada:
        if L not in codigo:
            texto = texto + L
        else:
            for P in range(len(codigo)):
                if L == mensagem_codificada[P]:
                    texto = texto + codigo[P]
        #caso nao encontre a letra no alfabeto deve manter a variavel original 
    return texto 


def main():
    menu()
    

if __name__=="__main__": 
    main()