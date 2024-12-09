
#for i in range(10):
   # print(i)
    #i=0 
#def FuncaoA():
    ##x = 0
    #while x < 10:
       # x = x + i
        #return x 
    
#print(FuncaoA)
#print(FuncaoA)
#print(FuncaoA)

def FunçãoB():
    x = 0
    while x < 10:
        x = x + 1 
        yield x #devolve o valor e mantém o estado 
for i in FunçãoB():
    print(i)
    i = 0