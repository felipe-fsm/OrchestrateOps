
# Comandos para Gerenciamento de Docker, Minikube, Kind, Kubernetes, Helm, Git e Docker Hub

Este documento reúne comandos importantes para gerenciar e operar Docker, Minikube, Kind, Kubernetes, Helm, Git e Docker Hub de forma eficiente.

---

## Comandos para Gerenciamento do Docker
### Iniciar o Serviço Docker
```bash
sudo systemctl start docker
```
Inicia o serviço Docker.

### Verificar o Status do Serviço Docker
```bash
sudo systemctl status docker
```
Verifica o status atual do serviço Docker.

### Reiniciar o Serviço Docker
```bash
sudo systemctl restart docker
```
Reinicia o serviço Docker.

### Parar o Serviço Docker
```bash
sudo systemctl stop docker
```
Para o serviço Docker.

### Comandos Gerais para Imagens e Contêineres
- **Listar imagens**:
  ```bash
  docker images
  ```
- **Remover uma imagem**:
  ```bash
  docker rmi nome-da-imagem
  ```
- **Construir uma imagem a partir de um Dockerfile**:
  ```bash
  docker build -t nome-da-imagem .
  ```

- **Listar contêineres em execução**:
  ```bash
  docker ps
  ```
- **Listar todos os contêineres**:
  ```bash
  docker ps -a
  ```

### Comando de Limpeza Completa do Docker
```bash
docker system prune --all --volumes --force
```
Remove todos os contêineres parados, imagens não utilizadas, redes e volumes.

### Limpeza Completa Avançada
**Remover diretórios de dados (CUIDADO: remove tudo relacionado ao Docker)**
```bash
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

Se você deseja desativar completamente o Docker, incluindo o `docker.socket`, você pode parar esse serviço com o comando:

```bash
sudo systemctl stop docker.socket
```

Para garantir que ele não seja iniciado automaticamente, você pode desativá-lo com:

```bash
sudo systemctl disable docker.service docker.socket
```

Isso impedirá que o Docker e o `docker.socket` sejam iniciados automaticamente até que você os inicie manualmente com:

```bash
sudo systemctl start docker.service
``` 

ou 

```bash
sudo systemctl start docker.socket
``` 

Use esses comandos conforme a necessidade para gerenciar os serviços do Docker.


---

## Comandos para Minikube
### Iniciar Minikube
```bash
minikube start
```
Inicia um cluster Minikube.

### Parar Minikube
```bash
minikube stop
```
Para o cluster Minikube.

### Verificar o Status do Minikube
```bash
minikube status
```
Exibe o status do cluster.

### Deletar o Cluster Minikube
```bash
minikube delete
```
Remove o cluster Minikube.


Use eval $(minikube docker-env) se você tem apenas um cluster do Minikube em execução ou está confortável em usar o padrão.
Use eval $(minikube -p minikube docker-env) se você está trabalhando com múltiplos perfis do Minikube e quer garantir que o ambiente Docker está configurado para um perfil específico.


---

## Comandos para Kind (Kubernetes in Docker)
### Criar um Cluster Kind
```bash
kind create cluster --name nome-do-cluster
```
Cria um cluster Kind.

### Excluir um Cluster Kind
```bash
kind delete cluster --name nome-do-cluster
```
Remove um cluster Kind específico.

---

## Comandos para Kubernetes
### Verificar a Versão do Kubernetes
```bash
kubectl version --client
```
Exibe a versão do `kubectl`.

### Listar Pods em Todos os Namespaces
```bash
kubectl get pods --all-namespaces
```

### Criar um Deployment
```bash
kubectl create deployment nome-do-deployment --image=nome-da-imagem
```

### Escalar um Deployment
```bash
kubectl scale deployment nome-do-deployment --replicas=3
```

### Deletar um Deployment
```bash
kubectl delete deployment nome-do-deployment
```

---

## Comandos para Helm
### Adicionar um Repositório de Charts
```bash
helm repo add nome-do-repo url-do-repo
```

### Instalar um Chart
```bash
helm install nome-da-release nome-do-repo/nome-do-chart
```

### Atualizar uma Release
```bash
helm upgrade nome-da-release nome-do-repo/nome-do-chart
```

### Deletar uma Release
```bash
helm uninstall nome-da-release
```

---

## Comandos Essenciais do Git
### Configuração Inicial
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### Criar um Repositório
```bash
git init
```

### Clonar um Repositório
```bash
git clone url-do-repositorio
```

### Adicionar e Fazer Commit
```bash
git add .
git commit -m "Mensagem do commit"
```

### Enviar Alterações para o Repositório Remoto
```bash
git push
```

---

## Comandos para Docker Hub
### Login no Docker Hub
```bash
docker login
```
Realiza login na sua conta Docker Hub.

### Criar uma Imagem Docker
```bash
docker build -t nome-da-imagem:tag .
```
Cria uma imagem Docker a partir de um `Dockerfile` no diretório atual (`.`). O `-t` permite nomear a imagem com um `nome-da-imagem` e opcionalmente especificar uma `tag`.

### Enviar uma Imagem para o Docker Hub
```bash
docker push nome-da-imagem:tag
```
Envia uma imagem local para o Docker Hub. Certifique-se de que a imagem tenha sido criada e esteja corretamente nomeada com o prefixo da sua conta Docker Hub (por exemplo, `usuario/nome-da-imagem`).

### Baixar uma Imagem do Docker Hub
```bash
docker pull nome-da-imagem:tag
```
Baixa uma imagem do Docker Hub. Se a `tag` não for especificada, a versão `latest` será baixada por padrão.

### Listar Imagens no Docker Hub
Não existe um comando direto pelo Docker CLI para listar imagens no Docker Hub, mas você pode ver suas imagens na [página do Docker Hub](https://hub.docker.com/).

### Exemplo Completo de Criação e Upload de uma Imagem:
1. **Crie a imagem a partir de um `Dockerfile`**:
   ```bash
   docker build -t usuario/nome-da-imagem:tag .
   ```
   Certifique-se de substituir `usuario` pelo nome de sua conta no Docker Hub.

2. **Verifique se a imagem foi criada**:
   ```bash
   docker images
   ```

3. **Realize login no Docker Hub (se necessário)**:
   ```bash
   docker login
   ```

4. **Envie a imagem para o Docker Hub**:
   ```bash
   docker push usuario/nome-da-imagem:tag
   ```

Isso garante que a imagem será disponibilizada publicamente (ou de forma privada, se configurado) no seu repositório do Docker Hub, pronta para ser compartilhada e baixada.

---

Esses comandos fornecem uma visão abrangente para gerenciar e operar ambientes de desenvolvimento com Docker, Minikube, Kind, Kubernetes, Helm, Git e Docker Hub de forma eficiente.

---


# Tutorial: Construindo e Subindo uma Imagem Docker para o Docker Hub

Este guia explica como criar uma imagem Docker a partir do seu projeto e fazer o upload para o Docker Hub.

## Pré-requisitos

1. **Docker** instalado em sua máquina. [Guia de instalação do Docker](https://docs.docker.com/get-docker/)
2. Conta no **Docker Hub**. [Cadastre-se no Docker Hub](https://hub.docker.com/signup)

---

## Passo 1: Logar no Docker Hub

Primeiro, faça login na sua conta Docker Hub:

```bash
docker login
```

Digite seu **nome de usuário** e **senha** quando solicitado.

---

## Passo 2: Navegar até o Diretório do Projeto

No terminal, vá para o diretório onde estão o `Dockerfile` e os arquivos da aplicação:

```bash
cd /caminho/para/o/seu/projeto
```

---

## Passo 3: Construir a Imagem Docker

Construa a imagem Docker usando o comando `docker build`. Substitua `felipesantosmachado` pelo seu nome de usuário do Docker Hub e `orchestrateops` pelo nome desejado para a imagem.

```bash
docker build -t felipesantosmachado/orchestrateops:latest .
```

- **`felipesantosmachado`**: Seu nome de usuário no Docker Hub.
- **`orchestrateops`**: Nome da imagem que você está criando.
- **`latest`**: Tag da imagem (por exemplo, `latest` ou `v1.0`).

---

## Passo 4: Adicionar uma Tag à Imagem (Opcional)

Se você já construiu a imagem sem especificar um nome de repositório e deseja adicionar uma tag, use:

```bash
docker tag orchestrateops:latest felipesantosmachado/orchestrateops:latest
```

---

## Passo 5: Verificar a Imagem Criada

Verifique se a imagem foi criada com sucesso usando:

```bash
docker images
```

A imagem recém-criada deve aparecer na lista.

---

## Passo 6: Subir a Imagem para o Docker Hub

Use o comando `docker push` para fazer o upload da imagem para o Docker Hub:

```bash
docker push felipesantosmachado/orchestrateops:latest
```

> Aguarde o upload ser concluído. A velocidade depende da sua conexão e do tamanho da imagem.

---

## Passo 7: Verificar no Docker Hub

Após o upload, vá até o Docker Hub e verifique se a imagem está disponível no seu repositório.

---

## Dicas Adicionais

- **Atualizar a Imagem**: Quando fizer alterações na sua aplicação, você pode recriar a imagem com uma nova `versao` (por exemplo, `v1.1`) e fazer o upload novamente.
- **Remover Imagens Locais**: Para liberar espaço, você pode remover imagens locais antigas com `docker rmi nome_da_imagem`.
- **Subir múltiplas tags**: Para subir diferentes versões da mesma imagem, repita o processo de tag e `docker push` com uma tag diferente, como `v1.1`.

---

Agora você aprendeu como construir e subir uma imagem Docker para o Docker Hub!