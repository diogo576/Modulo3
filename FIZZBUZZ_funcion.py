
 

#FIZZBUZZ se o numero for divisivel por 3 e 5 

#FIZZ se o numeros for divisivel 
def FIZZBUZZ(upTo):
    
    for n in range(1,upTo+1):
        if n % 3 == 0 and n % 5 ==0:
            print("FIZZBUZZ",end=" ")

FIZZBUZZ(35)

"""
def FIZZBUZZ_v3(upTo):
    for n in range(1,upTo+1)
    print("FIZZBUZZ"if n % 15 == 0 else "FIZZ" if n % 3 == 0 else "BUZZ" if n % 5 == 0 else str(n),end=" ")

"""