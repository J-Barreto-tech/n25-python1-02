"""
Arquivo que contera funções úteis ao sitema 
Author: Richard Brosler
"""
def cabecalho(titulo):
    colunas = 60
    espacos = (colunas-len(titulo)//2)
    texto = " " * espacos + titulo + " " * espacos    
    print(texto)


cabecalho("ola turma!")
