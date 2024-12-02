import utils

x = utils.ler_numero_inteiro()
print(x)

x = utils.ler_numero_inteiro("quantos são?")
print(x)

x = utils.ler_numero_inteiro_limites(-10,10,"introduza um nº inteiro:")
x = utils.ler_numero_inteiro_limites(0,1000)
x = utils.ler_numero_inteiro_limites(10)
x = utils.ler_numero_inteiro_limites(10,None,"introduza qualquer coisa:")

x = utils.ler_numero_inteiro_limites(-10,10,"introduza um valor decimal:")
x = utils.ler_numero_decimal_limites(0,10.5)
x = utils.ler_numero_decimal_limites(10.5)
x = utils.ler_numero_decimal_limites(0,None,"introduza um valor:")
