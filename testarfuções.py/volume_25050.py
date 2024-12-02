#Completa a função de acordo com a docstring
def Volume(L,A,C):
    """
    Recebe os 3 lados de um paralelepípedo e devolve o volume
    Parâmetro:
        largura, altura, comprimento: valores reais maiores que zero
    Devolve:
        None: se algum dos lados não tiver um valor válido
        real com 2 casas decimais com o valor do volume do cubo
    """
    if L < 0:
        return None 
    elif A < 0:
        return None 
    elif C < 0:
        return None 
    volume =( L * A * C )
    return round(volume,2) 
  
#Testes
assert Volume(1,1,1) == 1, "Erro a função devia devolver 1"
assert Volume(6,4,5) == 120, "Erro a função devia devolver 120"
assert Volume(-1,2,3) == None,"Erro a função devia devolver None"
assert Volume(1,-2,3) == None, "Erro a função devia devolver None"
assert Volume(1,2,-3) == None, "Erro a função devia devolver None"
assert Volume(1.5,2.5,3.5) == 13.12, "Erro a função devia devolver ??"

print("Função passou nos testes")