# Aula Hands-On: Kubernetes

Observação: abra o PowerShell como administrador.

---

## 1. Verificar se todos os requisitos estão instalados
  
    ```bash
    curl --version      # para confirmar a instalação do Curl.
    docker --version    # para confirmar a instalação do Docker.
    helm version        # para confirmar a instalação do Helm.
    kind version        # para confirmar a instalação do Kind.
    kubectl version     # para verificar se o Kubernetes está configurado.
    ```
    
    - Abra o Postman para verificar se ele está funcionando corretamente.

---

## 2. Baixar a aplicação OrchestrateOps do GitHub

1. **Baixar o programa OrchestrateOps**:
    - Acesse o link do repositório no GitHub: [https://github.com/felipe-fsm/OrchestrateOps.git](https://github.com/felipe-fsm/OrchestrateOps.git) e clique em **Code > Download ZIP** para baixar o arquivo compactado.

2. **Clonar o repositório via HTTPS**:
    - Como alternativa, você pode clonar o repositório diretamente com o comando:
        ```bash
        git clone https://github.com/felipe-fsm/OrchestrateOps.git
        ```

---

## 3. Limpar o Ambiente (Opcional)

1. **Remover todos os releases do Helm em todos os namespaces**:

    ```powershell
    helm list --all-namespaces | ForEach-Object { helm uninstall $_.Name --namespace $_.Namespace }
    ```
    - Substitua `_.Name` e `_.Namespace` pelas colunas adequadas, dependendo da saída do `helm list`.

2. **Deletar todos os recursos do Kubernetes em todos os namespaces**:

    ```powershell
    kubectl delete all --all --all-namespaces
    ```
    Este comando funciona nativamente no Windows, desde que o `kubectl` esteja configurado corretamente no sistema.

3. **Excluir todos os clusters do Kind**:
    ```powershell
    kind get clusters | ForEach-Object { kind delete cluster --name $_ }
    ```
    - A sintaxe do PowerShell utiliza `ForEach-Object` para iterar sobre os clusters retornados por `kind get clusters`.

4. **Limpeza total do Docker**:

    ```powershell
    docker system prune --all --volumes --force
    ```
    Este comando funciona nativamente no Windows, desde que o Docker Desktop esteja instalado.

5. **Parar o Docker e o socket do Docker**:

    No Windows, o Docker é geralmente gerenciado pelo Docker Desktop. Para parar o Docker:
        - No **Docker Desktop**: clique em "Stop Docker Desktop" no menu de configurações.
        - Via PowerShell:
            ```powershell
            (Get-Service -Name com.docker.service).Status
            Stop-Service -Name com.docker.service
            ```
    Este comando para o serviço do Docker no Windows.

---

## 4. Iniciar o ambiente no Windows

### **4.1. Iniciar o Docker**

No Windows, o Docker é gerenciado pelo **Docker Desktop**. Siga os passos abaixo:

#### Via Docker Desktop

    1. Abra o **Docker Desktop**:
        - Clique no menu Iniciar, procure por "Docker Desktop" e abra o aplicativo.
        - Aguarde enquanto ele inicia (pode levar alguns minutos).

    2. Verifique o status:
        - Certifique-se de que o ícone do Docker está ativo na barra de tarefas.
        - Para confirmar que o Docker está funcionando, abra o **PowerShell** e execute:
        ```powershell
        docker version
        ```
        Este comando deve retornar informações sobre o cliente e o daemon do Docker.

#### Via PowerShell

    ```powershell
    (Get-Service -Name com.docker.service).Status
    Stop-Service -Name com.docker.service
    ```


---

### **4.2. Criar um cluster Kind**

O processo para criar um cluster Kind no Windows é semelhante ao Linux. Certifique-se de que o **Kind** está instalado e configurado.

1. Navegue até o diretório onde está o arquivo de configuração do cluster:
   - No **PowerShell**, execute:
     ```powershell
     cd C:\caminho\para\o\arquivo\
     ```
     Substitua `C:\caminho\para\o\arquivo\` pelo caminho real onde o arquivo `kind-cluster-config.yaml` está localizado.

2. Execute o comando para criar o cluster Kind:
   ```powershell
   kind create cluster --name <nome-do-cluster> --config <nome-do-arquivo>.yaml
   ```
   Exemplo:
   ```powershell
   kind create cluster --name orchestrateops-cluster --config kind-cluster-config.yaml
   ```

   **Resultado esperado**: O Kind criará um cluster Kubernetes utilizando o Docker, de acordo com as especificações do arquivo `kind-cluster-config.yaml`.

---

### **4.3. Instalar o release do Helm**

Após criar o cluster, instale o release Helm para implantar a aplicação. Certifique-se de que o **Helm** está instalado no sistema.

1. Navegue até o diretório que contém o chart Helm:
   ```powershell
   cd C:\caminho\para\o\chart\
   ```
   Substitua `C:\caminho\para\o\chart\` pelo caminho real onde o chart Helm está localizado, por exemplo:
   ```powershell
   cd C:\cd-trabalho-kubernetes\OrchestrateOps\helm\orchestrateops-chart\
   ```

2. Instale o release Helm:
   ```powershell
   helm install <nome-da-release> .
   ```
   Exemplo:
   ```powershell
   helm install orchestrateops-release .
   ```

   Aqui:
   - **`orchestrateops-release`** é o nome do release.
   - O **`.`** indica que o chart Helm está no diretório atual.

   **Resultado esperado**: O Helm instalará o release no cluster Kubernetes, criando os recursos necessários (como deployments e serviços) para a aplicação.

---

## 5. Comandos úteis para Kubernetes

Aqui está uma seleção dos comandos Kubernetes mais utilizados na prática para verificar o estado de recursos em um cluster:

    ```powershell
    kubectl get namespaces
    kubectl get deployments
    kubectl get replicasets
    kubectl get pods
    kubectl get nodes
    kubectl get pv
    kubectl get pvc
    kubectl get events
    ```

Flag -n (Namespace): A flag -n permite especificar o namespace no qual o comando será executado.
Flag -o wide (Detalhes Ampliados): A flag -o wide altera o formato da saída padrão, adicionando informações extras sobre os recursos.
Flag -w (Watch/Monitoramento em Tempo Real): A flag -w permite que você monitore os recursos em tempo real. Quando usada, o comando continua em execução e atualiza a saída automaticamente sempre que houver uma mudança nos recursos monitorados.

---

## 6. Testes

### 6.1 Teste de Conectividade via Solicitação `GET` no Postman

1. Postman
2. GET
3. http://localhost:30010
4. Send

### 6.2 Teste de Criação via Solicitação `POST` no Postman

1. Postman
2. POST
3. http://localhost:30010/solicitacoes/
4. Body
5. raw
6. JSON
7.  {
        "id": 1,
        "setor": "Setor A",
        "solicitante": "Solicitante A",
        "produto": "Produto A",
        "quantidade": 5,
        "status": "pendente"
    }
8. Send

### 6.3. Teste de Leitura de Todas as Solicitações via Solicitação `GET` no Postman

1. Postman
2. GET
3. http://localhost:30010/solicitacoes/
4. Send

### 6.4. Teste de Leitura de uma Solicitação Específica via Solicitação `GET` no Postman

1. Postman
2. GET
3. http://localhost:30010/solicitacoes/1
4. Send

### 6.5. Teste de Atualização de uma Solicitação via Solicitação `PUT` no Postman

1. Postman
2. GET
3. http://localhost:30010/solicitacoes/1
4. Body
5. raw
6. JSON
7.  {
        "status": "em processamento"
    }
8. Send

### 6.6. Teste de Exclusão de uma Solicitação via Solicitação `DELETE` no Postman

1. Postman
2. DELETE
3. http://localhost:30010/solicitacoes/1
4. Send
5. GET
6. http://localhost:30010/solicitacoes/1
7. Send

### 6.7. Teste de Persistência de Dados

1. Postman
    1. GET
    2. http://localhost:30010/solicitacoes/
    3. Send
2. PowerShell
    1. helm uninstall orchestrateops-release
3. Postman
    1. GET
    2. http://localhost:30010/solicitacoes/
    3. Send
    4. Response: "Could not get response"
4. PowerShell
    1. helm install orchestrateops-release .
    2. "Aguarda um pouco para criação das estruturas da aplicação."
3. Postman
    1. GET
    2. http://localhost:30010/solicitacoes/
    3. Send
    4. Response: "200 OK"

### 6.7. Teste de Recuperação de Falhas de Nó

1. Powershell 1
    kubectl get nodes
    kubectl get pods -o wide
    kubectl get pods -o wide -w

1. PowerShell 2
    kubectl describe node orchestrateops-cluster-worker*
    kubectl delete node orchestrateops-cluster-worker*

2. Postman
    1. GET
    2. http://localhost:30010/solicitacoes/
    3. Send

2. Acompanhe o PowerShell 1

### 6.7. Teste de Recuperação de Falhas de Pod

1. Powershell 1
    kubectl get pods -o wide
    kubectl get pods -o wide -w

1. PowerShell 2
    kubectl delete pod orchestrateops-release-orchestrateops-*

    kubectl delete pod orchestrateops-release-orchestrateops-67bc896479-6f7vk

2. Postman
    1. GET
    2. http://localhost:30010/solicitacoes/
    3. Send

2. Acompanhe o PowerShell 1

### 6.8. Teste de Upgrade de Template Helm

1. PowerShell 1

    1. helm list
    2. kubectl get pods
    3. kubectl get services
    4. kubectl get replicasets -w

2. VSCode
    1. Atualize a quantidade de replicas no deployment.yaml (localizado em \OrchestrateOps\helm\orchestrateops-chart\templates)
    2. Salve o arquivo

3. PowerShell 2

    1. Navegue até o dir do Chart
    2. helm uninstall orchestrateops-release
    3. helm install orchestrateops-release .

3. Acompanhe o PowerShell 1

### 6.9. Teste Simplificado de Capacidade de Armazenamento (Storage) (Em desenvolvimento)

1. VSCode
    1. Comente/Descomente as linhas 14 e 15 do pv.yaml (localizado em \OrchestrateOps\helm\orchestrateops-chart\templates)
    2. Comente/Descomente as linhas 20 e 21 do pvc.yaml (localizado em \OrchestrateOps\helm\orchestrateops-chart\templates)

2. PowerShell 1

    1. Navegue até o dir do Chart
    2. helm uninstall orchestrateops-release
    3. helm install orchestrateops-release .

3. ...