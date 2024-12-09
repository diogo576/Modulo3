#programa para indicar a que quadrantes pertence um determinado ponto 
#pedir ao utilizador as coordenadas do ponto 

x = int(input("introduza um numero para  x:"))
y = int(input("introduza um numero para y:"))
def Quadrante(x,y):

    if x > 0 and y > 0:
            print("o ponto pertence ao 1º quadrante")
    if x < 0 and y > 0:
        print("o ponto pertence ao 2º quadrante")
    if x < 0 and y < 0:
        print("o ponto pertence ao 3º quadrante")
    if x > 0 and y < 0:
        print("o ponto pertence ao 4º quadrante")
    #testar se o ponto esta em cima de algum eixo 
    if x == 0 or y == 0:
        print(" o ponto está sobre os eixos")

