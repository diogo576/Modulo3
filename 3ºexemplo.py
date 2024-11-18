#valores de valores 
def saudação(texto="mundo"):
    print(f"olá,{texto}")

def saudação2(nome,parte_dia="bom dia"):
    print(f"{parte_dia},{nome}")

#saudação()
#saudação("juaquim")
saudação2(parte_dia="bom dia",nome="juaquim")
saudação2("boa tarde","Maria")
saudação2("juaquim")