Aqui está o `README.md` atualizado, agora incluindo as **Operações Básicas do GitHub** na seção de operações.

---

# OrchestrateOps

## Sumário
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Iniciando a Aplicação](#iniciando-a-aplicação)
- [Testando a Aplicação](#testando-a-aplicação)
- [Operações Básicas](#operações-básicas)
  - [Docker](#docker)
  - [Kubernetes](#kubernetes)
  - [Helm](#helm)
  - [GitHub](#github)

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
  Use o comando abaixo para criar solicitações com setores e solicitantes variados:

   ```bash
   curl -X POST "http://localhost:8080/solicitacoes/" -H "Content-Type: application/json" -d '{
     "setor": "Financeiro",
     "solicitante": "Maria Silva",
     "produto": "Notebook",
     "quantidade": 1,
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

## Operações Básicas

### Docker

#### Comandos Básicos

- **Listar Containers**:
  ```bash
  docker ps -a
  ```

- **Iniciar Docker**:
  ```bash
  sudo systemctl start docker
  ```

- **Parar Todos os Containers**:
  ```bash
  docker stop $(docker ps -q)
  ```

- **Remover Containers Parados**:
  ```bash
  docker rm -vf $(docker ps -aq)
  ```

#### Limpeza

- **Limpeza Completa do Docker** (remove todos os containers, imagens e volumes não utilizados):
  ```bash
  docker system prune -a --volumes -f
  ```

#### Solução de Problemas

- **Erro: `Cannot connect to the Docker daemon`**  
  **Solução**: Verifique se o Docker está em execução com `sudo systemctl status docker`. Se necessário, inicie-o com `sudo systemctl start docker`.

- **Imagem não encontrada (`ImagePullBackOff` ou `ErrImagePull` no Kubernetes)**  
  **Solução**: Certifique-se de ter executado `eval $(minikube docker-env)` antes de construir a imagem para que ela esteja disponível no ambiente do Minikube.

### Kubernetes

#### Comandos Básicos

- **Iniciar o Minikube**:
  ```bash
  minikube start
  ```

- **Listar Todos os Pods no Namespace Atual**:
  ```bash
  kubectl get pods
  ```

- **Reiniciar um Pod**:
  ```bash
  kubectl delete pod <nome-do-pod>
  ```

- **Descrever um Pod (detalhes do status)**:
  ```bash
  kubectl describe pod <nome-do-pod>
  ```

#### Limpeza

- **Remover Todos os Recursos no Kubernetes**:
  ```bash
  kubectl delete all --all --all-namespaces
  ```

- **Remover Namespaces Adicionais**:
  ```bash
  kubectl get namespaces
  kubectl delete namespace <nome-do-namespace>
  ```

#### Solução de Problemas

- **Erro: `Connection refused` ao tentar acessar a aplicação**  
  **Solução**: Verifique se o pod está em execução (`kubectl get pods`). Se o pod não estiver ativo, verifique os detalhes com `kubectl describe pod <nome-do-pod>`, e reconfigure o port forwarding.

- **Banco de dados não persiste após reiniciar o Pod**  
  **Solução**: Verifique o volume em `/app/data` e o mapeamento de volumes no Docker e Kubernetes. Certifique-se de que o `DATABASE_URL` está configurado para um caminho persistente.

### Helm

#### Comandos Básicos

- **Instalar uma Release**:
  ```bash
  helm install <nome-da-release> <caminho-do-chart>
  ```

- **Atualizar uma Release Existente**:
  ```bash
  helm upgrade <nome-da-release> <caminho-do-chart>
  ```

- **Listar Todas as Releases**:
  ```bash
  helm list --all-namespaces
  ```

- **Listar Releases em um Namespace Específico**:
  ```bash
  helm list --namespace <nome-do-namespace>
  ```

#### Limpeza

- **Desinstalar uma Release**:
  ```bash
  helm uninstall <nome-da-release>
  ```

- **Remover Todas as Releases e Repositórios do Helm**:
  ```bash
  helm ls --all --short | xargs -n 1 helm delete
  helm repo list --short | xargs -n 1 helm repo remove
  rm -rf ~/.cache/helm ~/.config/helm ~/.local/share/helm/plugins
  ```

#### Solução de Problemas

- **Release não foi desinstalada completamente (PVC não removido)**  
  **Solução**: Verifique se o PVC possui a anotação `"helm.sh/resource-policy": keep`, o que instrui o Helm a manter o PVC após a desinstalação. Para removê-lo manualmente, use `kubectl delete pvc <nome-do-pvc>`.

- **Erro: `Helm not found` ou falha ao instalar o chart**  
  **Solução**: Verifique se o Helm está instalado (`helm version`). Se não estiver, instale-o conforme a documentação oficial.

### GitHub

#### Comandos Básicos

- **Verificar o Status do Repositório**:
  ```bash
  git status
  ```

- **Adicionar Arquivos ao Staging**:
  - Para adicionar um arquivo específico:
    ```bash
    git add <nome-do-arquivo>
    ```
  - Para adicionar todas as alterações:
    ```bash
    git add .
    ```

- **Fazer um Commit das Alterações**:
  ```bash
  git commit -m "Descrição das alterações realizadas"
  ```

- **Enviar as Alterações para o Repositório Remoto**:
  ```bash
  git push origin <nome-da-branch>
  ```

#### Limpeza



- **Desfazer um Commit Localmente** (reverte o último commit mas mantém as alterações no staging):
  ```bash
  git reset --soft HEAD~1
  ```

- **Desfazer Alterações no Staging**:
  ```bash
  git reset
  ```

- **Remover Arquivos Localmente** (mas não no repositório remoto):
  ```bash
  git rm --cached <nome-do-arquivo>
  ```

#### Solução de Problemas

- **Erro: `detached HEAD`**  
  **Solução**: Verifique a branch em que está e retorne à branch principal com:
  ```bash
  git checkout main
  ```

- **Conflito de Merge**  
  **Solução**: Edite manualmente os arquivos para resolver os conflitos, então adicione as alterações e faça o commit.
  ```bash
  git add <arquivos-resolvidos>
  git commit -m "Resolvendo conflitos"
  ```

---

Esse `README.md` fornece um guia completo para configuração, inicialização, testes e operações de manutenção para a aplicação **OrchestrateOps**, incluindo instruções específicas para Docker, Kubernetes, Helm e GitHub. A seção de operações básicas está organizada para facilitar o gerenciamento e a resolução de problemas de forma eficiente.