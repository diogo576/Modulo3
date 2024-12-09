
def somar(x,y):
    print(x + y)
    x = 0
    y = 0

def main():
    somar("joaquim,maria")
    somar(10,5)
    somar(12.3,-3.2)
    n=10
    z=15
    somar(n,z)
    print(n,z)

if __name__=="__main__":
    main()

"""
 10
 11
 5
 6
 2
 3
 7
 2
 3
 8
 2
 3
 """