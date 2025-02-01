"""Uma função que recebe uma palavra e devolve a mesma palavra convertida na lingua dos P
Alguns exemplos:
    Casa  -> Capasapa
    Bola  -> Bopolapa
    Olá   -> Opolápá
    Muito -> Muipuitopo
"""
def E_vogal(letra:str)->bool:
    #função que devolve true/False se letra é vogal/consuante
    vogais="aeiouáàã"
    if letra.lower()in vogais:
        return True 
    return False 

def converteSilaba(silaba:str)->str:
    """função que recebe uma silaba e junta a mesma silaba na lingua dos p
    p.e: ca -> capa
        mui -> muipui
        o ->opo
    """
    if E_vogal(silaba[0]):
        silaba = silaba + "p" + silaba.lower()
    else:
        temp= ""
        for i in range(1,len(silaba)):
            temp =temp + silaba[i]
        silaba = silaba + temp 
    return silaba 


def coverte(palavra:str) ->str:
    """ função que converte uma palavra na lingua dos p"""
    converte = ""
    for i in range(len(palavra)):
        if E_vogal(palavra[i]== False and i> 0):
            
