#variável global
resultado= 0 
def soma(x,y):
    global resultado 
    resultado= x + y #está a criar uma variável local

soma(10,5)
print(resultado) 
