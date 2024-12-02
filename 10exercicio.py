#função que receba como parametros de entrada as medidas dos dois catetos de um triangulo retângulo
# e devolve a hipotenusa 
import math 

def função_hipotenusa(cateto1:float,cateto2:float)->float:
    hipotenusa = math.pow(cateto1,2) + math.pow(cateto2,2)
    hipotenusa = math.sqrt(cateto1**2+cateto2**2)
    return hipotenusa 

assert função_hipotenusa(4,3)== 5,"função devolve o valor errado"
print("função passou nos testes")
