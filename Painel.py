import requests
import os

def limpar():
    os.system('clear')

def cabecalho():
    print("="*40)
    print("      SISTEMA DE BUSCA AVANÇADA      ")
    print("="*40)

def consultar(tipo, valor):
    print(f"\n[~] Consultando {tipo}: {valor}...")
    
    # IMPORTANTE: Substitua 'SUA_API_AQUI' pelo link da sua API real
    # Exemplo: https://api.site.com/puxar?cpf={valor}&token=SEU_TOKEN
    token = "SEU_TOKEN_AQUI"
    url = f"https://api.exemplo.com/{tipo.lower()}?token={token}&query={valor}"
    
    try:
        # r = requests.get(url) # Comentei para não dar erro sem a API
        # if r.status_code == 200:
        #    dados = r.json()
        
        # Exemplo de como os dados aparecerão na tela:
        print("\n--- DADOS ENCONTRADOS ---")
        print(f"RESULTADO: [ Dados de {tipo} para {valor} ]")
        print("-" * 20)
        print("NOME COMPLETO: ...")
        print("CPF/CNPJ: ...")
        print("MÃE: ...")
        print("PAI: ...")
        print("NASCIMENTO: ...")
        print("ENDEREÇO: ...")
        print("-" * 20)
        
    except Exception as e:
        print(f"[!] Erro de conexão: {e}")

def menu():
    while True:
        limpar()
        cabecalho()
        print("[ 1 ] CONSULTAR CPF (Nome, Pais, Nasc)")
        print("[ 2 ] CONSULTAR NOME")
        print("[ 3 ] CONSULTAR NÚMERO")
        print("[ 4 ] CONSULTAR PLACA")
        print("[ 0 ] SAIR")
        print("="*40)
        
        op = input("\nEscolha a opção: ")
        
        if op == '0': break
        
        mapa = {'1': 'CPF', '2': 'NOME', '3': 'NUMERO', '4': 'PLACA'}
        
        if op in mapa:
            valor = input(f"Digite o {mapa[op]}: ")
            consultar(mapa[op], valor)
            input("\nPressione Enter para voltar ao menu...")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
