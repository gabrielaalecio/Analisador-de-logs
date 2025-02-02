#- Quantas requisições de cada método foram feitas?
#- Quais os IPs que mais acessaram?
#- Quantas requisições com status de erro tiveram?
#Crie suas próprias perguntas.
# - Quantos acessos deram certo?
import csv
from rich.console import Console
from rich.panel import Panel
import os
from time import sleep

console = Console()


def abrir_log():
    with open("weblog.csv", "r") as arquivo:
        leitor = list(csv.reader(arquivo))
    return leitor
    
def contar_metodos(log):
    contagem = {'GET': 0, 'POST': 0}
    for linha in log:
        if len(linha) > 2:
            divisao_linha = linha[2].split()
            metodo = divisao_linha[0]
            if metodo in ['GET', 'POST']:
                contagem[metodo] = contagem[metodo] + 1
    return contagem

def main():
    leitor = abrir_log()
    #inserir barra de carregamento (status)
    contagem = contar_metodos(leitor)
    print("Quantidade de métodos lidos: ")
    print(f"Get: {contagem['GET']}")
    print(f"Post: {contagem['POST']}")
    

main()