"""
Programa para calcular o vencimento de um trabalhador.
O programa deve começar por solicitar ao trabalhador que indique o seu nome, quantas horas trabalhou por dia, e quanto ganha por hora. 
Caso o trabalho tenho mais do que 8 horas de trabalho deve receber, por cada hora extra recebe mais 25%. Caso tenho trabalho 
mais do que 10 horas por dia deve receber 50% por cada hora além das 10 horas.
"""

def PedirNomeTrabalhador():
    """Esta função deve pedir o nome do trabalhador. O nome deve ter pelo menos 3 letras."""
    pass

def PedirHorasTrabalho():
    """Esta função pede ao utilizador quantas horas trabalho no dia. O nº de horas deve ser superior a zero."""
    pass

def PedirOrdenado():
    """Esta função pede ao utilizado quanto ganha por cada hora de trabalho"""
    pass

def MostrarVencimento(nome,horas,ordenado_por_hora):
    """Esta função deve mostrar o nome do trabalhador e quanto é que deve receber pelo dia de trabalho"""
    pass

def main():
    # Função principal do programa
    # pedir o nome do trabalhador
    nome = input("introduza o nome:")
    # pedir as horas que trabalhou
    horas = float("introduza o nºde horas que trabalhou:")
    # pedir o ordenado por hora
    ordenado_hora = float(input("introduza o salario por hora:"))
    # calcular e mostrar o vencimento

if __name__=="__main__":
    main() 