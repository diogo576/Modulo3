#a)uma função que caucula a media de 3 numeros inteiros.
#a função deve ler do utilizador os 3 numeros, caucular e mostrar a média 

def mediaA(x,y,z):
    x=int(input("x:"))
    y=int(input("y:"))
    z=int(input("z:"))
    media=(x + y + z)/3 
    print(f" a media é{media}")



#B)uma função que caucula a média de 3 numeros inteiros 
#A função deve receber os 3 numeros, caucular e mostrar a media 

def mediaB(x,y,z):
    media=(x + y + z)/3 
    print(f" a media é{media}")

#C) uma função que caucula a média de 3 numeros inteiros 
#a funçao deve ler do utilizador os 3 numeros, caucular e devolver a media 
def mediaC():
    x=int(input("x:"))
    y=int(input("y:"))
    z=int(input("z:"))
    media=(x + y + z)/3 
    return media # devolver o valor da media 

#D)uma função que caucula a média de 3 numeros inteiros 
#a função RECEBER os 3 números,caucula e devolve o valor 
def mediaD(x,y,z):
    media=(x + y + z)/3 
    return media 

def main():
    #mediaA()
    #n1=int(input("introduza um nº"))
    mediaB(5,5,5)
    print(f"a media é {mediaD(5,5,5)}")#chama a função e mostra o valor devolvido 
if __name__=="__main__":
    main()