import requests
import os

def menu():
    os.system('clear')
    print("="*35)
    print("      PAINEL DE CONSULTA v1.0    ")
    print("="*35)
    print("[ 9 ] CONSULTAR CPF")
    print("[ 2 ] CONSULTAR CEP (Endereço)")
    print("[ 3 ] CONSULTAR CNPJ (Empresa)")
    print("[ 0 ] SAIR")
    print("="*35)
    
    op = input("\nEscolha uma opção: ")

    if op == '9':
        cpf = input("Digite o CPF: ")
        print(f"\n[!] Consultando CPF: {cpf}")
        print("Nome: Leonardo Exemplo Melo")
        print("Endereço: Rua das Flores, 123")
        print("Cidade: São Paulo - SP")
        # Nota: Para dados reais, você precisaria colocar sua URL de API aqui
        input("\nPressione Enter para voltar...")

    elif op == '2':
        cep = input("Digite o CEP: ")
        r = requests.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")
        if r.status_code == 200:
            d = r.json()
            print(f"\nResultado:\nCidade: {d['city']}\nBairro: {d['neighborhood']}\nRua: {d['street']}")
        else:
            print("CEP não encontrado.")
        input("\nPressione Enter para voltar...")

    elif op == '3':
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
