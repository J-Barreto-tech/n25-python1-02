"""
Programa de teste de chamada com parametros no python
Version

"""
from click import clear 
#Definindo funções 
def calculo_variaveis(a,b):
    ret = a + b 
    a =15
    b =20
    return ret 
def uso_lista(list):
    list.append(5)
    list.append(6)
    return len(list)
# Programa principal 
d, e = 5,6
lista= [1,2]
# usando as funções 
clear()
print(calculo_variaveis(d,e))
print(d,e)
print("Antes: ", lista)
print(uso_lista(lista))
print("Depois:" , lista)