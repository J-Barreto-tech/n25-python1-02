"""
Programa de teste de escopo de variaveis -2 
Autor:

"""
from click import clear
def calculo():
    global c , d
    a = 5
    b = a+ c 
    c = 30 
    d = 50
    return b
#programa principal 
c=10
print(calculo())
print("Valor de c=",c)
