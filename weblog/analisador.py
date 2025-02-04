#- Quantas requisições de cada método foram feitas?
#- Quais os IPs que mais acessaram?
#- Quantas requisições com status de erro tiveram?
#Crie suas próprias perguntas.
# - Quantos acessos deram certo?
# - Qual dia teve mais acessos?
# - Qual horário teve mais acessos?
import csv
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich import print
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

def analisar_status(log):
    contagem_status = {}

    for linha in log:
        if len(linha) > 1:
            status = linha[3]

            if status in contagem_status:
                contagem_status[status] += 1
            else:
                contagem_status[status] = 1
    return contagem_status
            
def status_sucessos(contagem_status):
    contar = 0
    for i in contagem_status:
        if i.isdigit() and i != '404':
            contar = contar + contagem_status[i]
    return contar

def dia_mais_acessos(log):
    dias = {}
    for linha in log:
        if len(linha) > 2:
            divisao_linha = linha[1].split()
            data = divisao_linha[0].replace('[', '')[:11]
            if data in dias:
                dias[data] += 1
            else:
                dias[data]  = 1
    dia_mais_acessado = sorted(dias.items(), key=lambda x: x[1], reverse=True)
    return dia_mais_acessado[0][0]

def hora_mais_acessos(log):
    horas = {}
    for linha in log:
        if len(linha) > 2:
            divisao_linha = linha[1].split()
            hora = divisao_linha[0].replace('[', '')[12:14]
            if hora in horas:
                horas[hora] += 1
            else:
                horas[hora]  = 1
    hora_mais_acessado = sorted(horas.items(), key=lambda x: x[1], reverse=True)
    return hora_mais_acessado[0][0]

def main():
    leitor = abrir_log()
    for i in track(range(8), description="[green]Carregando...[/]"):
        sleep(2)

    print("\n[b red]Dados Analisados[/]\n")

    contagem = contar_metodos(leitor)
    print("[pink3]Quantidade de métodos lidos: [/]")
    print(f"Get: {contagem['GET']}")
    print(f"Post: {contagem['POST']}")

    contagem_ips = contar_ips(leitor)
    ips_ordenados = sorted(contagem_ips.items(), key=lambda x: x[1], reverse=True)
    
    print("\n[pink3]Top 5 IPs que mais acessaram:[/]")
    for ip, quantidade in ips_ordenados[:5]:  
        print(f"{ip}: {quantidade} acessos")

    contar_status = analisar_status(leitor)
    print(f"\n[pink3]Quantidade de status de erro: [/]{contar_status['404']}")
    print(f"[pink3]Quantidade de status bem-sucedidos: [/]{status_sucessos(contar_status)}")
    print(f"[pink3]Dia com maior quantidade de acessos: [/][b bright_cyan]{dia_mais_acessos(leitor)}[/]")
    print(f"[pink3]Horário com maior quantidade de acessos:[/] [b bright_cyan]{hora_mais_acessos(leitor)}hs[/]\n")

main()