import requests
import json
import shutil
import os
import time

# URL base da aplicação
BASE_URL = "http://localhost:8080/solicitacoes"

# Função para limpar o terminal (compatível com Windows, Mac e Linux)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de separador de seção
def print_separator():
    print("\n" + "*" * 40 + "\n")

# Função para exibir uma ordem específica
def display_order(order):
    print(f"ID: {order['id']}")
    print(f"Setor: {order['setor']}")
    print(f"Solicitante: {order['solicitante']}")
    print(f"Produto: {order['produto']}")
    print(f"Quantidade: {order['quantidade']}")
    print(f"Status: {order['status']}")
    print("-" * 40)

# Função para exibir ordens
def display_orders(orders):
    total_orders = len(orders)  # Conta o total de ordens
    print(f"Total de ordens: {total_orders}\n")  # Exibe o total no cabeçalho

    # Mostra os últimos três registros
    if total_orders > 3:
        print("  ...\n")
        orders_to_display = orders[-3:]  # Obtém os últimos três registros
    else:
        orders_to_display = orders

    for order in orders_to_display:
        display_order(order)

# Funções CRUD
def create_order():
    clear_terminal()
    print_separator()
    print("Criação de Ordem")
    setor = input("Setor: ")
    solicitante = input("Solicitante: ")
    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))

    data = {
        "setor": setor,
        "solicitante": solicitante,
        "produto": produto,
        "quantidade": quantidade,
        "status": "pendente"
    }

    response = requests.post(BASE_URL, headers={"Content-Type": "application/json"}, data=json.dumps(data))
    if response.status_code == 200:
        print("Ordem criada com sucesso!")
    else:
        print("Erro ao criar ordem:", response.text)
    print_separator()
    input("Pressione Enter para retornar ao menu principal...")

def read_order_by_id():
    clear_terminal()
    print_separator()
    print("Listagem de Ordem por ID")
    order_id = input("Digite o ID da ordem: ")
    response = requests.get(f"{BASE_URL}/{order_id}")

    if response.status_code == 200:
        order = response.json()
        display_order(order)
    else:
        print("Erro ao listar ordem:", response.text)
    print_separator()
    input("Pressione Enter para retornar ao menu principal...")

def read_orders():
    clear_terminal()
    print_separator()
    print("Listagem de Todas as Ordens")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        orders = response.json()
        display_orders(orders)
    else:
        print("Erro ao listar ordens:", response.text)
    print_separator()
    input("Pressione Enter para retornar ao menu principal...")

def update_order_status():
    clear_terminal()
    print_separator()
    print("Atualização de Status da Ordem")
    order_id = input("ID da ordem para atualizar: ")
    response = requests.get(f"{BASE_URL}/{order_id}")

    if response.status_code == 200:
        print("Status atual da ordem:", response.json().get("status"))
        
        print("Escolha o novo status:")
        print("1. Pendente")
        print("2. Em processamento")
        print("3. Finalizada")
        status_option = input("Digite o número do novo status: ")

        status_mapping = {
            "1": "pendente",
            "2": "em processamento",
            "3": "finalizada"
        }

        new_status = status_mapping.get(status_option)
        if new_status:
            update_data = {"status": new_status}
            update_response = requests.put(f"{BASE_URL}/{order_id}", headers={"Content-Type": "application/json"}, data=json.dumps(update_data))
            if update_response.status_code == 200:
                print("Status atualizado com sucesso!")
            else:
                print("Erro ao atualizar status:", update_response.text)
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Ordem não encontrada.")
    print_separator()
    input("Pressione Enter para retornar ao menu principal...")

def delete_order():
    clear_terminal()
    print_separator()
    print("Exclusão de Ordem")
    order_id = input("ID da ordem para excluir: ")
    response = requests.delete(f"{BASE_URL}/{order_id}")
    if response.status_code == 200:
        print("Ordem excluída com sucesso!")
    else:
        print("Erro ao excluir ordem:", response.text)
    print_separator()
    input("Pressione Enter para retornar ao menu principal...")

# Função para criação automática de ordens
def create_orders_repeatedly(max_orders=100000):
    clear_terminal()
    print(f"Criação Automática de Ordens (Limite: {max_orders} ordens)")

    counter = 1  # Inicializa o contador

    while counter <= max_orders:
        setor = f"Setor {counter}"  # Nome do setor concatenado com o contador
        solicitante = f"Solicitante {counter}"  # Nome do solicitante concatenado com o contador
        quantidade = counter  # Quantidade igual ao contador
        produto = f"Produto Teste {counter}"  # Nome do produto com o contador

        data = {
            "setor": setor,
            "solicitante": solicitante,
            "produto": produto,
            "quantidade": quantidade,
            "status": "pendente"
        }

        response = requests.post(BASE_URL, headers={"Content-Type": "application/json"}, data=json.dumps(data))
        if response.status_code == 200:
            print(f"Ordem '{produto}' criada com sucesso!")
            counter += 1  # Incrementa o contador
        else:
            print("Erro ao criar ordem:", response.text)

        time.sleep(0.01)  # Aguardar meio segundo antes da próxima criação

    print("Criação automática concluída.")

    print_separator()
    input("Pressione Enter para retornar ao menu principal...")

# Função para exclusão automática de ordens
def delete_orders_repeatedly():
    clear_terminal()
    print("Exclusão Automática de Ordens (Pressione Ctrl+C para parar)")
    
    while True:
        # Obter a lista de ordens
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            orders = response.json()
            if orders:
                order_id = orders[0]["id"]  # Seleciona o primeiro ID para deletar
                delete_response = requests.delete(f"{BASE_URL}/{order_id}")
                if delete_response.status_code == 200:
                    print(f"Ordem {order_id} excluída com sucesso!")
                else:
                    print("Erro ao excluir ordem:", delete_response.text)
            else:
                print("Nenhuma ordem disponível para exclusão.")
        else:
            print("Erro ao obter ordens:", response.text)

        time.sleep(0.5)  # Aguardar meio segundo antes da próxima exclusão

    print("Exclusão automática interrompida.")

# Função do menu com opções automáticas
def menu():
    while True:
        clear_terminal()
        print("Menu CRUD de Ordens:")
        print("1. Criar Ordem")
        print("2. Listar Ordem por ID")
        print("3. Listar Todas as Ordens")
        print("4. Atualizar Status de Ordem")
        print("5. Excluir Ordem")
        print("6. Iniciar Criação Automática de Ordens")
        print("7. Iniciar Exclusão Automática de Ordens")
        print("8. Sair")
        
        option = input("Escolha uma opção: ")

        if option == "1":
            create_order()
        elif option == "2":
            read_order_by_id()
        elif option == "3":
            read_orders()
        elif option == "4":
            update_order_status()
        elif option == "5":
            delete_order()
        elif option == "6":
            max_orders = int(input("Quantas ordens deseja criar? "))
            create_orders_repeatedly(max_orders)
        elif option == "7":
            delete_orders_repeatedly()
        elif option == "8":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu diretamente
if __name__ == "__main__":
    menu()
