def ler_numero_inteiro(mensagem="introduza um valor inteiro:")->int:
    """
    função que le do utilizador um nº inteiro. a função garante que o valor inserido é um valor válido
    """
    while True:
        dados = input(mensagem)
        #verificar se existe um traço no inicio da string
        if dados[0] == "-":
            testar = dados.replace("-","")
        else:
            testar = dados 
        
        if testar.isdigit():
            return int(dados)
        print("Erro:o valor inserido não é válido")


def ler_numero_inteiro_limites(valor_min,valor_max=None,mensagem="introsuza um valor:"):
    """
    função que recebe o valor minimo e maximo a ler do utilizador.
    A função devolve o valor quando é inteiro válido  
    """
    while True:
        numero = ler_numero_inteiro(mensagem)
        if numero >= valor_min and (valor_max is None or numero <=valor_max):
            return numero
        print("Erro: O valor não é válido.")





def ler_numero_decimal(mensagem="introduza um valor decimal:")->float:
    """
    função para ler um numero decimal.A função garante que o valor é valido 

    """
    while True:
        dados = input(mensagem)
        if len(dados)==0:
            continue
         #substituir as virgulas pr pontos 
        dados=dados.replace("-",".")

        #verificar se existe um traço no inicio da string
        if dados[0] == "-":
            testar = dados.replace("-","")
        else:
            testar = dados 
        testar = testar.replace(",",".")
        #contar os pontos decimais 
        pontos = testar.count(".")
        #remover os pontos decimais 
        testar = testar.replace(".","")
        # não pode ter mais do que 1 ponto decimal e só pode ter digitos 
        if testar.isdigit()and pontos<=1:
            return float(dados)
        print("Erro: O valor não é válido")


def ler_numero_decimal_limites(valor_min,valor_max=None,mensagem="inroduza um valor:")->float:
    while True:
        valor = ler_numero_decimal(mensagem)
        if valor >= valor_min and (valor_max is None or valor <= valor_max):
            return valor 
        print("Erro:valor não é válido")