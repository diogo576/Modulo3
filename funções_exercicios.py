# Exercício de Funções em Python
# Complete cada função conforme indicado na docstring.
import

def imprimir_dobro(valor):
    """Recebe um número e imprime o seu dobro."""
    dobro = valor * 2 
    print(dobro)
    
print(imprimir_dobro(3))

	
def calcular_media_tres_numeros(n1, n2, n3):
    """
    Calcule a média aritmética de três números.
    Retorne o valor da média.
    """
    media = (n1 + n2 + n3)/3
    return media 
print(calcular_media_tres_numeros(2,4,6))
	
def calcular_fatorial(numero):
    """Recebe um número inteiro positivo e retorna o seu fatorial.
	    Fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1
	""" 
    factorial = 1 
    for n in range(1,numero+1):
        fatorial = fatorial * n
        return factorial 
    
	
def converter_celsius_para_fahrenheit(celsius):
    """
    Converta a temperatura de Celsius para Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    return (celsius * 9/5) + 32 

def calcular_area_circulo(raio):
    """
    Calcule a área de um círculo dado o raio.
    Use pi = 3.14159
    """
    area = math.pi * raio **2 
    return area 


def exibir_contagem_regressiva(inicio):
    """Recebe um número e imprime uma contagem regressiva até 0."""
    for i in range(inicio,-1,-1):
        print(i)


def inverter_string(texto):
    """
    Receba uma string e retorne ela invertida.
    Exemplo: "python" -> "nohtyp"
    """
    for i in range(len(texto),-1,-1):
        texto_invertido = texto_invertido + texto[i]
    return texto_invertido


def verificar_divisibilidade(a, b):
    """Recebe dois números e imprime se o primeiro é divisível pelo segundo."""
    resto= a % b 
    if resto ==0:
        print("é divisivel")
    else:
        print("nao é divisivel")


def calcular_perimetro_circulo(raio):
    """Recebe o raio de um círculo e retorna o seu perímetro."""
    perimetro = 2 * math.pi * raio 
    return perimetro 

def converter_segundos_para_minutos(segundos):
    """Recebe um valor em segundos e retorna o correspondente em minutos."""
    minutos = segundos// 60
    segundos_restam = segundos %60
    return f""

def gerar_saudacao_periodo():
    """
    Retorne uma saudação baseada no período do dia.
    Se for antes de 12h: "Bom dia!"
    Entre 12h e 18h: "Boa tarde!"
    Após 18h: "Boa noite!"
    """
    hora = datetime.now().hour 
    if hora > 18:
        return "boa noite"
    elif hora <12 :

        return "bom dia"
    else:
        return "boa tarde"


def calcular_desconto(preco, percentual):
    """Recebe um preço e um percentual de desconto e retorna o preço com desconto."""
    percentagem_pagar = 100 - percentual 
    preco_com_desconto = preco * percentagem_pagar / 100
    return preco_com_desconto
print(calcular_desconto(100,100))

    

    
def calcular_velocidade_media(distancia, tempo):
    """Recebe a distância percorrida e o tempo gasto e retorna a velocidade média."""
    velocidade_media = 0
    velocidade_media = distancia / tempo 
    return velocidade_media

print(calcular_velocidade_media(20,10))

def verificar_palindromo(palavra):
    """
    Verifique se a palavra recebida é um palíndromo.
    Palíndromo é uma palavra que pode ser lida igual de trás para frente.
    Exemplo: "radar" é um palíndromo.
    """
    resultado = palavra == inverter_string(palavra)
    return resultado 


