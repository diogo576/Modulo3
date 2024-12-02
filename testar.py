import utils

x = utils.ler_numero_inteiro()
print(x)

x = utils.ler_numero_inteiro("quantos são?")
print(x)

x = utils.ler_numero_inteiro_limites(-10,10,"introduza um nº inteiro:")
x = utils.ler_numero_inteiro_limites(0,1000)
x = utils.ler_numero_inteiro_limites(10)
x = utils.ler_numero_inteiro_limites(10,None,"introduza qualquer coisa:")
x