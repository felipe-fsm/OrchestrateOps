Aqui está o `README.md` atualizado, incluindo as seções para a limpeza completa de Kubernetes e Helm.

---

# OrchestrateOps

## Sumário
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Iniciando a Aplicação](#iniciando-a-aplicação)
- [Testando a Aplicação](#testando-a-aplicação)
- [Possíveis Problemas e Soluções](#possíveis-problemas-e-soluções)
- [Operações Básicas](#operações-básicas)
- [Limpeza Completa](#limpeza-completa)

---

## Configuração do Ambiente

1. **Certifique-se de que todos os requisitos estão instalados**:
   Verifique se você possui `Docker`, `Minikube`, `Kubectl`, `Helm` e `curl` instalados e configurados. Execute os comandos abaixo para confirmar as versões instaladas:

   ```bash
   docker --version         # Docker
   minikube version         # Minikube
   kubectl version --client # Kubectl
   helm version             # Helm
   curl --version           # Curl
   ```

2. **Inicie o Docker**:
   - Inicie o Docker Desktop (para Windows ou Mac) ou inicie o serviço Docker no Linux:
     ```bash
     sudo systemctl start docker
     ```

3. **Inicie o Minikube**:
   - Emule um cluster Kubernetes local:
     ```bash
     minikube start
     ```

4. **Configure o Docker para Usar o Minikube**:
   - Direcione a construção de imagens para o Minikube:
     ```bash
     eval $(minikube docker-env)
     ```

## Iniciando a Aplicação

1. **Construa a Imagem Docker da Aplicação**:
   - A partir da pasta `OrchestrateOps`, construa a imagem:
     ```bash
     docker build -t orchestrateops .
     ```

2. **Inicie o Helm**:
   - Navegue até `OrchestrateOps/helm` e instale o chart com o nome de release desejado (exemplo: `orchestrateops-release`):
     ```bash
     helm install orchestrateops-release ./orchestrateops-chart
     ```

3. **Verifique se os Pods estão em Execução**:
   - Confirme se os pods estão ativos:
     ```bash
     kubectl get pods
     ```

4. **Configurar o Port Forwarding para Acesso Local**:
   - Localize o nome do pod com `kubectl get pods` e execute:
     ```bash
     kubectl port-forward pod/<nome-do-pod> 8080:80
     ```

## Testando a Aplicação

### Testes de CRUD

1. **Criação de uma Solicitação (POST)**:
   - Crie novas solicitações com os seguintes comandos para diferentes setores e solicitantes:

   ```bash
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Financeiro",
     "solicitante": "Maria Silva",
     "produto": "Notebook",
     "quantidade": 1,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Compras",
     "solicitante": "João Souza",
     "produto": "Impressora",
     "quantidade": 2,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "TI",
     "solicitante": "Ana Costa",
     "produto": "Cabo HDMI",
     "quantidade": 5,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Marketing",
     "solicitante": "Pedro Lima",
     "produto": "Projetor",
     "quantidade": 1,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Vendas",
     "solicitante": "Carla Fernandes",
     "produto": "Tablet",
     "quantidade": 3,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Financeiro",
     "solicitante": "Luiz Alves",
     "produto": "Calculadora",
     "quantidade": 10,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "RH",
     "solicitante": "Juliana Ribeiro",
     "produto": "Cadeira Ergonômica",
     "quantidade": 4,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Logística",
     "solicitante": "Ricardo Martins",
     "produto": "Estante de Arquivo",
     "quantidade": 2,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "TI",
     "solicitante": "Fernanda Dias",
     "produto": "Roteador",
     "quantidade": 1,
     "status": "pendente"
   }'
   
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Compras",
     "solicitante": "Marcelo Vieira",
     "produto": "Cartucho de Tinta",
     "quantidade": 8,
     "status": "pendente"
   }'
   ```

2. **Listagem de Solicitações (GET)**:
   ```bash
   curl -X GET "http://localhost:8080/solicitacoes/"
   ```

3. **Atualização de uma Solicitação (PUT)**:
   - Altere o status de uma solicitação:
   ```bash
   curl -X PUT "http://localhost:8080/solicitacoes/1" -H "Content-Type: application/json" -d '{
     "status": "em processamento"
   }'
   ```

4. **Exclusão de uma Solicitação (DELETE)**:
   - Exclua uma solicitação específica:
   ```bash
   curl -X DELETE "http://localhost:8080/solicitacoes/1"
   ```

### Teste de Persistência

1. **Reinicie o Pod para Testar a Persistência**:
   ```bash
   kubectl delete pod <nome-do-pod>
   ```

2. **Reconfigure o Port Forwarding**:
   ```bash
   kubectl port-forward pod/<novo-nome-do-pod> 8080:80
   ```

3. **Verifique a Persistência (GET)**:
   ```bash
   curl -X GET "http://localhost:8080/solicitacoes/"
   ```

## Possíveis Problemas e Soluções

- **Erro: `Cannot connect to the Docker daemon`**
  - **Solução**: Verifique se o Docker está em execução com `sudo systemctl status docker`. Se não estiver, inicie-o com `sudo systemctl start docker`.

- **Erro: `Connection refused` ao tentar acessar a aplicação**
  - **Solução**: Verifique se o pod está em execução (`kubectl get pods`). Se o pod não estiver ativo, veja detalhes com `kubectl describe pod <nome-do-pod>` e certifique-se de que o port forwarding está configurado.

- **Erro: `ImagePullBackOff` ou `ErrImagePull` no Kubernetes**
  - **Solução**: Confirme que `eval $(minikube docker-env)` foi executado antes de construir a imagem para disponibilizá-la no Minikube. Reinstale o chart Helm, se necessário.

- **Banco de dados não persiste após reiniciar o Pod**
  - **Solução**: Verifique o volume em `app/data` e o mapeamento de volumes no Docker e Kubernetes. Certifique-se de que o `DATABASE_URL` está apontando para um caminho persistente.

- **Erro `Helm not found` ou falha ao instalar o chart**
  - **Solução**: Verifique a instalação do Helm (`helm version`). Se não estiver instalado, siga o guia oficial para instalá-lo.

---

## Operações Básicas

### Docker

1. **Iniciar o Docker**:
   ```bash
   sudo systemctl start docker
   ```

2. **Iniciar e Construir Containers com `docker-compose`

**:
   ```bash
   docker-compose up --build -d
   ```

3. **Parar Todos os Containers**:
   ```bash
   docker stop $(docker ps -q)
   ```

4. **Remover Todos os Containers Parados**:
   ```bash
   docker rm -vf $(docker ps -aq)
   ```

5. **Limpeza Completa do Docker**:
   ```bash
   docker system prune -a --volumes -f
   ```

### Kubernetes (`kubectl`)

1. **Iniciar o Minikube**:
   ```bash
   minikube start
   ```

2. **Listar Todos os Pods no Namespace Atual**:
   ```bash
   kubectl get pods
   ```

3. **Reiniciar um Pod**:
   ```bash
   kubectl delete pod <nome-do-pod>
   ```

4. **Descrever um Pod (Detalhes do Pod)**:
   ```bash
   kubectl describe pod <nome-do-pod>
   ```

### Helm

1. **Instalar um Chart**:
   ```bash
   helm install <nome-da-release> <caminho-do-chart>
   ```

2. **Atualizar uma Release Existente**:
   ```bash
   helm upgrade <nome-da-release> <caminho-do-chart>
   ```

3. **Limpar Configurações Locais do Helm**:
   ```bash
   helm repo remove <nome-do-repo>
   rm -rf ~/.cache/helm ~/.config/helm ~/.local/share/helm/plugins
   ```

---

## Limpeza Completa

### Docker

Para remover todos os containers, imagens, volumes e redes:

```bash
docker system prune -a --volumes -f
```

### Kubernetes

Para remover todos os recursos Kubernetes, incluindo Pods, Deployments, Services e ConfigMaps:

```bash
kubectl delete all --all --all-namespaces
```

Se desejar uma limpeza completa dos recursos e namespaces personalizados, você pode listar e excluir todos os namespaces adicionais:

```bash
kubectl get namespaces
kubectl delete namespace <nome-do-namespace>
```

### Helm

Para deletar todas as releases e repositórios do Helm, siga estas etapas:

1. **Remover todas as releases**:
   ```bash
   helm ls --all --short | xargs -n 1 helm delete
   ```

2. **Remover todos os repositórios**:
   ```bash
   helm repo list --short | xargs -n 1 helm repo remove
   ```

3. **Limpar o cache e configurações locais do Helm**:
   ```bash
   rm -rf ~/.cache/helm ~/.config/helm ~/.local/share/helm/plugins
   ```

Esses comandos garantirão uma limpeza completa, removendo todos os recursos e configurações locais, deixando o ambiente preparado para novas implementações.

---

Este guia cobre a configuração, operação, testes de CRUD, persistência e uma limpeza completa para a aplicação **OrchestrateOps** com Docker, Kubernetes e Helm, além de fornecer instruções detalhadas para operações básicas e solução de problemas.

Abaixo está uma sequência resumida para limpar o ambiente e realizar todas as etapas de instalação, execução e testes para o **OrchestrateOps**.

---

## Sugestão de Testes - Sequência Resumida de Operações para OrchestrateOps

### 1. Limpeza Completa do Ambiente

#### Docker
```bash
docker system prune -a --volumes -f
```

#### Kubernetes
```bash
kubectl delete all --all --all-namespaces
kubectl delete namespace <custom-namespace>  # Remova namespaces adicionais, se houver
```

#### Helm
```bash
helm ls --all --short | xargs -n 1 helm delete
helm repo list --short | xargs -n 1 helm repo remove
rm -rf ~/.cache/helm ~/.config/helm ~/.local/share/helm/plugins
```

### 2. Configuração do Ambiente

1. **Inicie o Docker**:
   ```bash
   sudo systemctl start docker
   ```

2. **Inicie o Minikube**:
   ```bash
   minikube start
   ```

3. **Configurar o Docker para Usar o Minikube**:
   ```bash
   eval $(minikube docker-env)
   ```

### 3. Construção e Publicação da Imagem Docker

1. **Construa a Imagem Docker da Aplicação**:
   - Na pasta `OrchestrateOps`, execute:
     ```bash
     docker build -t orchestrateops .
     ```

2. **Suba a Imagem para o Docker Hub**:
   ```bash
   docker login
   docker tag orchestrateops <seu_usuario>/orchestrateops:latest
   docker push <seu_usuario>/orchestrateops:latest
   ```

3. **Baixe a Imagem do Docker Hub (opcional em outro ambiente)**:
   ```bash
   docker pull <seu_usuario>/orchestrateops:latest
   ```

### 4. Instalação do Helm

1. **Instale o Chart com o Helm**:
   - Navegue até a pasta `OrchestrateOps/helm` e execute:
     ```bash
     helm install orchestrateops-release ./orchestrateops-chart
     ```

### 5. Configurar Port Forwarding para Acesso Local

1. **Verifique se os Pods estão em Execução**:
   ```bash
   kubectl get pods
   ```

2. **Configurar o Port Forwarding**:
   ```bash
   kubectl port-forward pod/<nome-do-pod> 8080:80
   ```

### 6. Testes de CRUD

1. **Criação de uma Solicitação (POST)**:
   ```bash
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Financeiro",
     "solicitante": "Maria Silva",
     "produto": "Notebook",
     "quantidade": 1,
     "status": "pendente"
   }'
   ```

2. **Listagem de Solicitações (GET)**:
   ```bash
   curl -X GET "http://localhost:8080/solicitacoes/"
   ```

3. **Atualização de uma Solicitação (PUT)**:
   ```bash
   curl -X PUT "http://localhost:8080/solicitacoes/1" -H "Content-Type: application/json" -d '{
     "status": "em processamento"
   }'
   ```

4. **Exclusão de uma Solicitação (DELETE)**:
   ```bash
   curl -X DELETE "http://localhost:8080/solicitacoes/1"
   ```

### 7. Teste de Persistência

1. **Reinicie o Pod para Testar a Persistência**:
   ```bash
   kubectl delete pod <nome-do-pod>
   ```

2. **Reconfigure o Port Forwarding**:
   ```bash
   kubectl port-forward pod/<novo-nome-do-pod> 8080:80
   ```

3. **Verifique a Persistência (GET)**:
   ```bash
   curl -X GET "http://localhost:8080/solicitacoes/"
   ```

---

Essa sequência cobre desde a limpeza do ambiente até os testes de CRUD e persistência da aplicação **OrchestrateOps** com Docker, Minikube, Kubernetes e Helm.