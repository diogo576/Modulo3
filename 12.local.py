#o programa deve ler do utilizador o nº de mesas e o nº de clientes que o restaurante pode receber 

"""
menu de opeções:
entrada 
saida 
estado 
terminar 
"""
import utils 

#def configurar():
    #funçao pere definir a configuração (nº de mesas e nº de clientes)


def entrada_clientes(n_max_clientes,n_atual_clientes):
    #responsavel por ler e registar a entrada dos clientes 
    #testar se o restaurante nao pode receber mais clientes
    if n_max_clientes ==n_atual_clientes:
        print("restaurante cheio")
        return 0 
    #ler o nº de clientes a entrar
    lugar_livres = n_max_clientes - n_atual_clientes
    entrar =utils.ler_numero_inteiro_limites(1,lugar_livres,"quantos clientes:")
    #devolve o nº de clientes que entraram 
    return entrar 

def entrada_mesas(n_max_mesas,n_atual_mesas):
    #testar se nao tem mesas livres
    if n_max_mesas == n_atual_mesas:
        print("restaurante cheio")
        return 0
    mesas_livres = n_max_mesas - n_atual_mesas
    entrar =utils.ler_numero_inteiro_limites(1,mesas_livres,"quantas mesas:")
    return entrar
    #responsavel por ler e registar a ocupação das mesas 
    

def saidaClientes(n_atual_clientes):
    #responsavel por registar a saida dos clientes 

    if n_atual_clientes == 0:
        print("não tem clientes")
        return 0
    n_clientes = utils.ler_numero_decimal_limites(1,n_atual_clientes,"quantos clientes saíram do restaurante")
    return n_clientes


def saidaMesas(n_atual_mesas,):
    # responsavel por registar as mesas desocupadas 
    if n_atual_mesas == 0:
        print("não tem mesas ocupadas")
        return 0
    n_mesas = utils.ler_numero_inteiro_limites(1,n_atual_mesas,"quantas mesas estao desocupadas")
    return n_mesas 
def estado(n_max_clientes,n_max_mesas,n_atual_mesas,n_atual_clientes,n_mesas,n_clientes,total_pago):
    print(n_atual_clientes)
    #calcula e mostra os dados estatisticos do estado do restuarante 
    print(f"tem {n_mesas} mesas ocupadas e {n_max_mesas} mesas livres")
    print(f"tem{n_clientes} clientes no restaurante ")
    print(f"que corresponde a uma ocupação de {n_clientes/n_max_clientes*100}%")
    print(f"já recebeu {total_pago}$ das refeições servidas")
  


def menu():
    n_max_mesas = utils.ler_numero_inteiro("nº de mesas do restaurante:")
    n_max_clientes = utils.ler_numero_inteiro("quantos clientes podem estar no restuarante:")
    opcao = 1
    #n_mesas e clientes atualmente no restaurante
    n_atual_mesas = 0 
    n_atual_clientes = 0  
    while opcao != 4:
        opcao = utils.ler_numero_inteiro_limites(1,4,"1.entrada\n2.saída\n3.estado\n4.terminar")
        if opcao== 1:
            #entrada dos clientes
            n_clientes_entraram = entrada_clientes(n_max_clientes,n_atual_clientes)
            n_mesas_ocupadas = entrada_mesas(n_max_mesas,n_atual_mesas)
            n_atual_clientes = n_atual_clientes + n_clientes_entraram 
            n_atual_mesas = n_atual_mesas + n_mesas_ocupadas
        if opcao == 3:
            estado(n_max_clientes,n_max_mesas,n_atual_mesas,n_atual_clientes)
            #saída de clientes
        if opcao == 2:
            n_clientes_sairam = saidaClientes(n_atual_clientes)
            n_mesas_desocupadas = saidaClientes(n_atual_mesas)
            n_atual_clientes = n_atual_clientes - n_clientes_sairam
            n_atual_mesas = n_atual_mesas - n_mesas_desocupadas
            #evitar o custo da refeição quando não saiu nenhum cliente do restuarante 
            if n_clientes_sairam > 0 or n_mesas_desocupadas>0:
                pagou = utils.ler_numero_decimal_limites(0,None,"quanto custou a refeição:")
                total_pago = total_pago - pagou 
        if opcao == 1:
            estado(n_max_mesas,n_max_clientes,n_atual_mesas,n_atual_clientes,total_pago)


def main():
    menu()

if __name__=="__main__":
    main()