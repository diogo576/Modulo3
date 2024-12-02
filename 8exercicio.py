import datetime

#parque de estacionamento 
"""
15 minutos 
preço?
ler hora:minutos de entrada 
calcular custo
"""

def duraçãoestacionamento(hora:int,minutos:int)->int:
#função que calcula a duração do estacionamento em minutos com base nos valores dos parametros e a hora atual
    hora_atual = datetime.datetime.now().hour 
    minutos_atuais = datetime.datetime.now().minute 
    n_horas = hora_atual - hora 
    n_minutos = minutos_atuais - minutos 
    if n_minutos < 0:
        n_horas = 1
        n_minutos = 60 - minutos - minutos_atuais
    duração_total_minutos = n_horas * 60 + n_minutos
    return duração_total_minutos
def blocosminutos(minutos:int)-> int:
    #função que recebe a duração em minutos e devolve quantos blocos de 15 minutos existem
    n_blocos = minutos // 15
    if minutos % 15 != 0:
        n_blocos == 1
    return n_blocos


def custo(blocos:int,preço_bloco:float)->float:
#função que calcula o custo do estacionamento com base na duração em minutos e o preço por cada bloco de 15 minutos
    return blocos * preço_bloco


def main():
    #ler dados 
    preço = float(input("qual é o preço a pagar por cada 15 minutos:"))
    hora =int(input("qual é a hora que entrou no parque:"))
    minutos = int(input("quais os minutos de entrada no parque:"))
    #calcular a duração em minutos 
    duração_minutos = duraçãoestacionamento(hora,minutos)
    blocos = blocosminutos(duração_minutos)
    print(duração_minutos)
    #calcular o custo
    custo = custo(blocos,preço)
    print(f"estacionamento com duração de{duração_minutos}que corresponde a {blocos}de 15 minutos 
          com custo de{custo}")
    
