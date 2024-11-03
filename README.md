

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

### 1. Verificar Requisitos

Certifique-se de que os seguintes componentes estão instalados e configurados: **Docker**, **Minikube**, **Kubectl**, **Helm** e **curl**. Confirme as versões instaladas com os comandos abaixo:

```bash
docker --version         # Docker
minikube version         # Minikube
kubectl version --client # Kubectl
helm version             # Helm
curl --version           # Curl
```

### 2. Iniciar Docker e Minikube

- **Inicie o Docker**:
  ```bash
  sudo systemctl start docker
  ```

- **Inicie o Minikube** para criar um cluster Kubernetes local:
  ```bash
  minikube start
  ```

- **Configure o Docker para usar o Minikube**:
  ```bash
  eval $(minikube docker-env)
  ```

## Iniciando a Aplicação

1. **Construir a Imagem Docker da Aplicação**:
   - Na pasta `OrchestrateOps`, execute:
     ```bash
     docker build -t orchestrateops .
     ```

2. **Subir a Imagem para o Docker Hub** (opcional, se precisar compartilhar):
   ```bash
   docker login
   docker tag orchestrateops <seu_usuario>/orchestrateops:latest
   docker push <seu_usuario>/orchestrateops:latest
   ```

3. **Instalar o Chart com o Helm**:
   - Navegue para a pasta `OrchestrateOps/helm` e execute:
     ```bash
     helm install orchestrateops-release ./orchestrateops-chart
     ```

4. **Configurar Port Forwarding para Acesso Local**:
   - Verifique os pods em execução:
     ```bash
     kubectl get pods
     ```

   - Configure o port forwarding:
     ```bash
     kubectl port-forward pod/<nome-do-pod> 8080:80
     ```

## Testando a Aplicação

### 1. Testes CRUD

- **Criação de uma Solicitação (POST)**:
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

- **Listagem de Solicitações (GET)**:
  ```bash
  curl -X GET "http://localhost:8080/solicitacoes/"
  ```

- **Atualização de uma Solicitação (PUT)**:
  ```bash
  curl -X PUT "http://localhost:8080/solicitacoes/1" -H "Content-Type: application/json" -d '{
    "status": "em processamento"
  }'
  ```

- **Exclusão de uma Solicitação (DELETE)**:
  ```bash
  curl -X DELETE "http://localhost:8080/solicitacoes/1"
  ```

### 2. Teste de Persistência

1. **Reinicie o Pod** para verificar persistência:
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
  **Solução**: Verifique se o Docker está em execução com `sudo systemctl status docker`. Se necessário, inicie-o com `sudo systemctl start docker`.

- **Erro: `Connection refused` ao acessar a aplicação**  
  **Solução**: Verifique os pods em execução (`kubectl get pods`). Certifique-se de que o port forwarding está configurado.

- **Erro: `ImagePullBackOff` ou `ErrImagePull` no Kubernetes**  
  **Solução**: Execute `eval $(minikube docker-env)` antes de construir a imagem. Reinstale o chart Helm se necessário.

- **Banco de dados não persiste após reiniciar o Pod**  
  **Solução**: Verifique o volume em `app/data` e o mapeamento de volumes no Docker e Kubernetes. Certifique-se de que o `DATABASE_URL` aponta para um caminho persistente.

---

## Operações Básicas

### Docker

- **Listar Containers**:
  ```bash
  docker ps -a
  ```

- **Iniciar Docker**:
  ```bash
  sudo systemctl start docker
  ```

- **Iniciar Containers com `docker-compose`**:
  ```bash
  docker-compose up --build -d
  ```

- **Parar Todos os Containers**:
  ```bash
  docker stop $(docker ps -q)
  ```

- **Remover Containers Parados**:
  ```bash
  docker rm -vf $(docker ps -aq)
  ```

- **Limpeza Completa do Docker**:
  ```bash
  docker system prune -a --volumes -f
  ```

### Kubernetes

- **Iniciar o Minikube**:
  ```bash
  minikube start
  ```

- **Listar Pods no Namespace Atual**:
  ```bash
  kubectl get pods
  ```

- **Reiniciar um Pod**:
  ```bash
  kubectl delete pod <nome-do-pod>
  ```

- **Descrever um Pod**:
  ```bash
  kubectl describe pod <nome-do-pod>
  ```

### Helm

- **Instalar um Chart**:
  ```bash
  helm install <nome-da-release> <caminho-do-chart>
  ```

- **Atualizar uma Release**:
  ```bash
  helm upgrade <nome-da-release> <caminho-do-chart>
  ```

- **Limpar Configurações Locais do Helm**:
  ```bash
  helm repo remove <nome-do-repo>
  rm -rf ~/.cache/helm ~/.config/helm ~/.local/share/helm/plugins
  ```

---

## Limpeza Completa

### Docker

Para remover containers, imagens, volumes e redes:

```bash
docker system prune -a --volumes -f
```

### Kubernetes

Para remover todos os recursos (Pods, Deployments, Services, ConfigMaps):

```bash
kubectl delete all --all --all-namespaces
```

Remover namespaces adicionais:

```bash
kubectl get namespaces
kubectl delete namespace <nome-do-namespace>
```

### Helm

Para deletar todas as releases e repositórios:

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

### GitHub

Para subir as alterações de um arquivo para o Git, siga os passos abaixo:

1. **Verificar o status do repositório** (opcional):
   ```bash
   git status
   ```

2. **Adicionar as alterações ao staging**:
   - Para adicionar um arquivo específico:
     ```bash
     git add nome_do_arquivo
     ```
   - Para adicionar todas as alterações:
     ```bash
     git add .
     ```

3. **Fazer um commit das alterações**:
   ```bash
   git commit -m "Descrição das alterações realizadas"
   ```

4. **Enviar as alterações para o repositório remoto**:
   ```bash
   git push origin nome_da_branch
   ```

   > Substitua `nome_da_branch` pela branch onde você está trabalhando (geralmente `main` ou `master`, ou uma branch específica).

### Resumo dos comandos:
```bash
git add .
git commit -m "Descrição das alterações"
git push origin nome_da_branch
```

Esses passos garantem que suas alterações sejam salvas localmente e enviadas para o repositório remoto.

-