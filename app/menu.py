import requests
import json
import shutil
import os
import time

# URL base da aplicação
# BASE_URL = "http://localhost:8080/solicitacoes"
BASE_URL = "http://localhost:30010/solicitacoes/"

# Função para limpar o terminal (compatível com Windows, Mac e Linux)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de separador de seção
def print_separator():
    print("\n" + "*" * 40 + "\n")

# Função para exibir uma ordem específica
def display_order(order):
    print("-" * 20)
    print(f"  ID: {order['id']}")
    print(f"  Setor: {order['setor']}")
    print(f"  Solicitante: {order['solicitante']}")
    print(f"  Produto: {order['produto']}")
    print(f"  Quantidade: {order['quantidade']}")
    print(f"  Status: {order['status']}")

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
    response = requests.get(f"{BASE_URL}{order_id}")

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
    response = requests.get(f"{BASE_URL}{order_id}")

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
            update_response = requests.put(f"{BASE_URL}{order_id}", headers={"Content-Type": "application/json"}, data=json.dumps(update_data))
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
    response = requests.delete(f"{BASE_URL}{order_id}")
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

# Função para simular o teste de replicação por consumo de CPU
def simulate_cpu_scalability_test(max_orders=None, delay=None):
    """
    Simula um teste de replicação criando ordens repetidamente, gerando carga para acionar o escalonamento de pods por consumo de CPU.

    Parâmetros:
    - max_orders: Número total de ordens a serem criadas no teste.
    - delay: Intervalo (em segundos) entre cada requisição, ajustável para intensificar ou aliviar a carga.
    """
    max_orders = max_orders or 1000  # Valor padrão de 1000 ordens
    delay = delay or 0.01  # Valor padrão de 0.01 segundos

    counter = 1  # Inicializa o contador

    while counter <= max_orders:
        setor = f"Setor {counter}"
        solicitante = f"Solicitante {counter}"
        quantidade = counter
        produto = f"Produto Teste {counter}"

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

        # Aguarda o tempo definido entre requisições para controlar a carga gerada
        time.sleep(delay)

    print("Teste de replicação por consumo de CPU concluído.")

# Função para simular o teste de replicação por consumo de memória
def simulate_memory_scalability_test(duration=None, chunk_size=None):
    """
    Simula o consumo de memória alocando blocos de dados para aumentar o uso de memória, gerando carga para acionar o escalonamento de pods por consumo de memória.

    Parâmetros:
    - duration: Duração total do teste em segundos.
    - chunk_size: Tamanho de cada bloco de dados alocado (em bytes), ajustável para intensificar ou aliviar a carga.
    """
    duration = duration or 60  # Valor padrão de 60 segundos
    chunk_size = chunk_size or 10**6  # Valor padrão de 1MB

    memory_load = []  # Lista para armazenar blocos de dados
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            memory_load.append("X" * chunk_size)  # Adiciona blocos de dados
            print(f"Memória consumida: {len(memory_load) * chunk_size / (1024**2):.2f} MB")
            time.sleep(0.1)  # Intervalo entre alocações
    except MemoryError:
        print("Erro de memória: teste de consumo de memória interrompido.")
    finally:
        print("Teste de replicação por consumo de memória concluído.")

# Funções de teste para limitação de recursos
def test_cpu_limit():
    print("Teste de Limitação de CPU iniciado...")
    load = 0
    try:
        while True:
            load += 1  # Cria carga constante de CPU
            if load % 1000000 == 0:
                print("Carga de CPU aplicada...")
    except KeyboardInterrupt:
        print("Teste de Limitação de CPU concluído.")
    print_separator()

def test_memory_limit():
    print("Teste de Limitação de Memória iniciado...")
    memory_load = []
    try:
        while True:
            memory_load.append("X" * 10**6)  # Adiciona 1MB de dados a cada iteração
            print(f"Memória consumida: {len(memory_load)} MB")
            time.sleep(0.5)  # Intervalo para observar o consumo no cluster
    except MemoryError:
        print("Limite de Memória atingido.")
    except KeyboardInterrupt:
        print("Teste de Limitação de Memória concluído.")
    print_separator()

# Função do menu principal
def menu():
    while True:
        clear_terminal()
        print("Menu OrchestrateOps:\n")
        print("  1. Criar Ordem")
        print("  2. Listar Ordem por ID")
        print("  3. Listar Todas as Ordens")
        print("  4. Atualizar Status de Ordem")
        print("  5. Excluir Ordem")
        print("  6. Iniciar Criação Automática de Ordens")
        print("  7. Iniciar Exclusão Automática de Ordens")
        print("  8. Teste de Replicação por Consumo de CPU (Não funcionou)")
        print("  9. Teste de Replicação por Consumo de Memória (Não funcionou)")
        print(" 10. Teste de Limitação de CPU")
        print(" 11. Teste de Limitação de Memória")
        print(" 12. Sair\n")
        
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
            # max_orders = input("Número de ordens para criar no teste de replicação por CPU (padrão 1000): ")
            # max_orders = int(max_orders) if max_orders else None
            # delay = input("Intervalo entre requisições (em segundos, padrão 0.01): ")
            # delay = float(delay) if delay else None
            # simulate_cpu_scalability_test(max_orders=max_orders, delay=delay)

            print("Esse teste de replicação por consumo de CPU não funcionou conforme planejado.")
            print_separator()

        elif option == "9":
            # duration = input("Duração do teste de replicação por memória (em segundos, padrão 60): ")
            # duration = int(duration) if duration else None
            # chunk_size = input("Tamanho do bloco de memória (em bytes, padrão 1048576): ")
            # chunk_size = int(chunk_size) if chunk_size else None
            # simulate_memory_scalability_test(duration=duration, chunk_size=chunk_size)

            print("Esse teste de replicação por consumo de memória não funcionou conforme planejado.")
            print_separator()

        elif option == "10":
            test_cpu_limit()
        elif option == "11":
            test_memory_limit()
        elif option == "12":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu diretamente
if __name__ == "__main__":
    menu()