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

def contar_ips(log):
    contagem_ips = {}
    
    for linha in log:
        if len(linha) > 1:  
            ip = linha[0]  
            
            if ip in contagem_ips:
                contagem_ips[ip] += 1
            else:
                contagem_ips[ip] = 1
    
    return contagem_ips


def main():
    leitor = abrir_log()
    #inserir barra de carregamento (status)
    contagem = contar_metodos(leitor)
    print("Quantidade de métodos lidos: ")
    print(f"Get: {contagem['GET']}")
    print(f"Post: {contagem['POST']}")

    contagem_ips = contar_ips(leitor)
    
    ips_ordenados = sorted(contagem_ips.items(), key=lambda x: x[1], reverse=True)
    
    print("\nTop 5 IPs que mais acessaram:")
    for ip, quantidade in ips_ordenados[:5]:  
        print(f"{ip}: {quantidade} acessos")
    

main()