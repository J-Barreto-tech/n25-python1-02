"""
Código para demonstrar escopo de variaveis no pyton


"""

from click import clear
#definindo uma função
def calculo():
    a = 5
    b = a + c 
    #c = 30 # se decomnetado dá erro porque a varial "c" passa ser local
    return b
#Programa principal
c = 10
clear()
print(calculo())

