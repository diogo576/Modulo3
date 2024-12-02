"""
dois numeros primos gémeos são dos numeros primos que distam em
 2 unidades um do outrp
 p.ex:
 3 e 5 
 5 e 7 
 fazer um programa que lê dois nº inteiros positivos do utilizador 
 e diz se são primos e primos gémeos 
"""
import exercicio4
from utils import ler_numero_inteiro

#ler dois numeros inteiros positivos 
n1=ler_numero_inteiro("introduza um nuemro inteiro:")
n2=ler_numero_inteiro("introduza outro nuemro inteiro:")
#testar se são primos
if exercicio4.exercicio4(n1) and exercicio4.exercicio4(n2):
#caucular a diferença 
    diferença = n1 - n2
    if abs(diferença) == 2:
        print(f"os valores {n1} e {n2} são primos gémeos")
    else:
     print(f"os valores {n1} e {n2} são primos") 

else:
    if exercicio4.exercicio4(n1):
      print(f"o valor{n1} é primo")
    elif exercicio4.exercicio4(n2):
       print(f"o valor {n2} é primo")
    else:
       print("nenhum dos valores é primo")
        

