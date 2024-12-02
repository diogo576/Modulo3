#função com o nome de soma_quadrados que recebe um número inteiro positivo 
#devolve a soma dos quadrados de todos os numeros inteiros positivos ate n 
import exercicio11

def soma_quadrados(n:int)->int:
    soma =0
    for i in range(1,n):
        q = exercicio11.função_quadrado(i)
        soma = soma + q
    return soma 

assert soma_quadrados(3) == 14,"valor devolvido devia ser 14"
assert soma_quadrados(5) == 15,"valor devolvido devia ser 55"
print("a função passou nos testes")