import math 
from datetime import datetime
def funcao_complicada():
    for i in range(1000000):
        _ = i ** 2 

#calcula a exponenciação utilizando a função pow do modulo math 
def funcao_complicada2():
    for i in range (1000000):
        _ = math.pow(i,2)

def medir_tempo():
    inicio = datetime.now()
    funcao_complicada2()
    fim = datetime.now()
    tempo_execucao = fim - inicio 
    print("tempo de execuçao:",tempo_execucao.total_seconds())

medir_tempo()
 