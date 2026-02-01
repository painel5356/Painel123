import requests
import os
import time

# Configuração de Cores
L = '\033[1;37m' # Branco
A = '\033[1;34m' # Azul
V = '\033[1;32m' # Verde
R = '\033[1;31m' # Vermelho
C = '\033[1;36m' # Ciano
Y = '\033[1;33m' # Amarelo
F = '\033[0m'    # Reset

def limpar():
    os.system('clear')

def banner():
    print(f"{A}="*45)
    print(f"{V}        SISTEMA DE BUSCA - PAINEL 123")
    print(f"{A}="*45 + f"{F}")

def buscar(tipo, valor):
    limpar()
    banner()
    print(f"{Y}[~] Consultando {tipo}: {valor}...{F}")
    time.sleep(1) # Simula um carregamento
    
    # ESTRUTURA DE EXIBIÇÃO
    print(f"\n{V}--- [ DADOS ENCONTRADOS ] ---{F}")
    print(f"{C}NOME: {L}LEONARDO CAMPOS MELO")
    print(f"{C}CPF: {L}{valor if tipo == 'CPF' else '000.xxx.xxx-00'}")
    print(f"{C}DATA NASC: {L}01/01/1990")
    print(f"{C}NOME MÃE: {L}MARIA DAS GRAÇAS MELO")
    print(f"{C}NOME PAI: {L}JOSÉ MELO")
    print(f"{C}ENDEREÇO: {L}RUA DAS PALMEIRAS, 45")
    print(f"{C}CIDADE/UF: {L}SÃO PAULO / SP")
    print(f"{C}CEP: {L}01001-000")
    
    if tipo == 'PLACA':
        print(f"{C}VEÍCULO: {L}HONDA CIVIC - PRETO")
        print(f"{C}CHASSI: {L}9BWXXXXXXXXXXXXXX")

    print(f"{V}------------------------------{F}")
    input(f"\n{Y}Pressione Enter para voltar ao Menu...{F}")

def menu():
    while True:
        limpar()
        banner()
        print(f"{V}[ 9 ]{L} CONSULTAR CPF")
        print(f"{V}[ 2 ]{L} CONSULTAR NOME")
        print(f"{V}[ 3 ]{L} CONSULTAR NÚMERO")
        print(f"{V}[ 4 ]{L} CONSULTAR PLACA")
        print(f"{R}[ 0 ] SAIR DO PAINEL{F}")
        print(f"{A}="*45 + f"{F}")
        
        escolha = input(f"{Y}Escolha uma opção: {F}")
        
        if escolha == '0':
            print(f"{R}Saindo...{F}")
            break
            
        mapa = {'9': 'CPF', '2': 'NOME', '3': 'NUMERO', '4': 'PLACA'}
        
        if escolha in mapa:
            dado = input(f"Digite o {mapa[escolha]}: ")
            buscar(mapa[escolha], dado)
        else:
            print(f"{R}Opção inválida!{F}")
            time.sleep(1)

if __name__ == "__main__":
    menu()
    cnpj = input("Digite o CNPJ: ")
        r = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
        if r.status_code == 200:
            d = r.json()
            print(f"\nEmpresa: {d['razao_social']}\nStatus: {d['descricao_situacao_cadastral']}")
        else:
            print("CNPJ não encontrado.")
        input("\nPressione Enter para voltar...")

    elif op == '0':
        exit()

if __name__ == "__main__":
    while True:
        menu()
