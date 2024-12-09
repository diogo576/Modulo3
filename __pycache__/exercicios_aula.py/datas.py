import datetime 
#data de hoje 
print(datetime.date.today())

#ano
print(datetime.date.today().year)
#mes 
print(datetime.date.today().month)
#data e hora 
print(datetime.datetime.now())
#como string
print(datetime.datetime.now().strptime("%d - %m - %y %h %M: %S"))