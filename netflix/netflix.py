#Qual perfil é mais usado?
#Qual o titulo mais acessado?
#Que dia foi mais acessado?
#De qual pais tem mais acessos?
#Maior tempo logado
#Perfil x: horas de netflix no total
#Horas no total da conta
import csv
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich import print
import os
from time import sleep

console = Console()

def contar_ocorrencias(log, index, slice_range=None):
    contagem = {}
    for linha in log[1:]:
        if len(linha) > index:
            valor = linha[index]
            if slice_range:
                valor = valor.split()[0].replace('[', '')[slice_range[0]:slice_range[1]]
            
            contagem[valor] = contagem.get(valor, 0) + 1
    
    return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

def abrir_log():
    with open("All_ViewingActivity.csv", "r", encoding="utf-8") as arquivo:
        leitor = list(csv.reader(arquivo))
    return leitor

def contar_perfis(log):
   return (contar_ocorrencias(log,0))

def contar_titulos(log):
    return contar_ocorrencias(log, 4)

def dia_mais_acessos(log):
    return contar_ocorrencias(log, 1, (0, 11))[0][0]

def contar_pais(log):
    return contar_ocorrencias(log, 9)[0][0]

def main():
    leitor = abrir_log()

    #barra carregamento
    for i in track(range(8), description="[green]Carregando...[/]"):
        sleep(0.5)

    contagem_perfis = contar_perfis(leitor)

    print("\n[b orange3]Top 5 Perfis mais acessados:[/]")
    for perfil, quantidade in contagem_perfis[:5]:  
        print(f"[b deep_pink4]{perfil}[/]: {quantidade} acessos")

    titulos_ordenados = contar_titulos(leitor)
    titulo_mais_assistido = titulos_ordenados[0][0] if titulos_ordenados else "Nenhum dado disponível"

    print(f"\n[b orange3]Título mais assistido:[/] [b deep_pink4]{titulo_mais_assistido}[/]")

    print(f"\n[b orange3]Dia mais acessado:[/] [b deep_pink4]{dia_mais_acessos(leitor)}[/]")

    print(f"\n[b orange3]País com mais acessos:[/] [b deep_pink4]{contar_pais(leitor)}[/]")

    

main()