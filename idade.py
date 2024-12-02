import datetime 

dia=int(input("dia de nascimento"))
mes=int(input("mes de nascimento"))
ano=int(input("ano de nascimento"))

hoje= datetime.date.today()

data_nascimento =datetime.date(dia,mes,ano)

idade= hoje.year - data_nascimento.year 
#verificar se nao fez anos este ano
if data_nascimento.month > hoje.month or data_nascimento.month == hoje.month and data_nascimento.day > hoje.day:
    idade= 1 

print(idade) 
