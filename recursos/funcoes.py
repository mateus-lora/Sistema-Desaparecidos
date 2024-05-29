from os import system; from time import sleep

def limparTela():
    system("cls")
    
def aguarde(segundos):
    sleep(segundos)
    
def verificaBancoDeDados():
    try:
        arquivo = open("database.mrs","r")
        arquivo.close()
        return ""
    except:
        arquivo = open("database.mrs","w")
        arquivo.close()
        return "Banco de Dados Criado com Sucesso!"
        