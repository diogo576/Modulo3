#valor return 
def soma(x,y):
    t= x + y 
    #se x e y forem 0:
    print(id(x))
    x= 0  #este valor nao será alterado no x global 
    print(id(y))
    y=0
    return t 

x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
t = soma(x,soma(y,z))
print(t)