"""
Arquivo que contera funções úteis ao sitema 
Author: Richard Brosler
"""

def cabecalho(titulo="Olá mundo!", colunas=60):
    #colunas = 60
    espacos = (colunas-len(titulo))//2
    texto = " " * espacos + titulo + " " * espacos    
    print(texto)

def fatorial(valor):
    ret = 1
    for i in range(valor,1,-1):
        ret *= i
    return ret # retorna o valor

def fatorial_rec(valor): #Fatorial usando recursividade
    if valor == 1: return 1
    return valor * fatorial_rec

if __name__ == "__main__": # só executa quando chamar o funcoes.py
    cabecalho("ola turma!",20)
