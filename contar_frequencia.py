"""
#para cada letra do alfabeto portugues, indique o n de vezes que aparece na frase 
sugestão:
    utilizar as funções ord() ou chr() para percorrer o alfabeto 
print(ord("a"))
print(chr(97))
"""
def ContarLetras(letra,frase):
    #função para contar quantas vezes a letra aparece na frase 
    contar = 0
    for l in frase:
        if letra == l:
            contar = contar + 1
    return contar 
def contarFrequencia(frase):
    #função que mostra o nº de vezes que cada letra do alfabeto aparece na frase
    #percorrer o alfabeto 
    for i in range(97,123):
        contar = ContarLetras(chr(i),frase)
        print(contar)
frase =input("introduza uma frase:")
contarFrequencia(frase)
    #chmara a função 
    #mostrar o que a função devolveu 