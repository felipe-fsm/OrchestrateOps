# Aula Hands-On: Kubernetes

---

## O que é uma aula Hands-On?

Uma aula *hands-on* é um formato de aprendizado prático.  
Nela, você aprende fazendo e aplicando os conceitos em tempo real.  
Durante a aula, serão propostas atividades que ajudam a consolidar o conteúdo.  

Hoje, nosso tema principal é **Kubernetes**.

---

## O que é Kubernetes?

Kubernetes é uma plataforma de orquestração de contêineres.  
Ele ajuda a automatizar a implantação, o escalonamento e o gerenciamento de aplicações em contêineres.  
Com Kubernetes, podemos gerenciar múltiplos contêineres em diferentes ambientes.  
Essa plataforma foi originalmente criada pelo Google e é mantida pela Cloud Native Computing Foundation (CNCF).
A documentação oficial do Kubernetes pode ser encontrada em [kubernetes.io/docs](https://kubernetes.io/docs).

### Comparação entre Kubernetes, Docker Swarm, OpenShift e Mesos

| Característica                | Kubernetes             | Docker Swarm         | OpenShift                   | Mesos                    |
|-------------------------------|------------------------|----------------------|-----------------------------|--------------------------|
| **Orquestração**              | Completa e robusta     | Simples e rápida     | Baseada em Kubernetes       | Modular e escalável      |
| **Escalabilidade**            | Alta                   | Média                | Alta                        | Muito Alta               |
| **Configuração de Rede**      | Complexa, mas flexível | Simples              | Simplificada com suporte    | Flexível e customizável  |
| **Interface de Usuário**      | CLI e Dashboard        | CLI                  | Dashboard e CLI             | CLI                      |
| **Segurança**                 | Alta, com suporte RBAC | Baixa                | Alta, com foco em segurança | Customizável             |
| **Ecossistema e Comunidade**  | Muito grande           | Menor                | Forte, empresarial          | Menor, especializado     |
| **Suporte a Multi-Cloud**     | Sim                    | Limitado             | Sim                         | Sim                      |
| **Uso Típico**                | Ambientes complexos    | Projetos simples     | Grandes empresas            | Grandes infraestruturas  |

---

## O que é OrchestrateOps

OrchestrateOps é uma aplicação de controle de solicitações de compra, permitindo gerenciar ordens, via uma API REST simples com persistência de dados em SQLite. A aplicação opera em contêineres Docker e demonstra funcionalidades de orquestração de containers usando Kubernetes e Helm, facilitando operações de criação, leitura, atualização e exclusão (CRUD) e oferecendo testes de escalabilidade e resiliência."

---

## Etapas da Aula

Durante esta aula, exploraremos o Kubernetes em detalhes, entenderemos seu funcionamento e faremos exercícios práticos para aplicá-lo.

### 1. Configuração do Ambiente

#### 1.1. Requisitos e Dependências

- **Curl**: ferramenta de linha de comando que permite realizar requisições HTTP, útil para interagir diretamente com APIs e testar endpoints.
  [Documentação Curl](https://curl.se/docs/)

- **Docker**: plataforma de contêineres que facilita a criação, o empacotamento e a execução de aplicações de forma isolada e consistente.
  [Documentação Docker](https://docs.docker.com/)

- **Helm**: gerenciador de pacotes para Kubernetes que simplifica a implantação e a atualização de aplicações no cluster, usando pacotes chamados *charts*.
  [Documentação Helm](https://helm.sh/docs/)

- **Kubernetes**: sistema de orquestração de contêineres que automatiza a implantação, escalonamento e gerenciamento de aplicações em contêineres.
  [Documentação Kubernetes](https://kubernetes.io/docs/)

- **Kubernetes Dashboard**: interface gráfica que permite visualizar e gerenciar os recursos do cluster Kubernetes, incluindo pods, serviços e status geral.
  [Documentação Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

- **Minikube**: ferramenta que permite rodar Kubernetes localmente, ideal para desenvolvimento e testes em um ambiente de cluster em um único nó.
  [Documentação Minikube](https://minikube.sigs.k8s.io/docs/)

- **Postman**: ferramenta que facilita a criação, teste e documentação de APIs, permitindo enviar requisições HTTP e visualizar respostas.
  [Documentação Postman](https://learning.postman.com/docs/getting-started/introduction/)

##### Verificação dos Requisitos e Dependências

1. **Verifique se todos os requisitos estão instalados**:
    ```bash
    curl --version      # para confirmar a instalação do Curl.
    docker --version    # para confirmar a instalação do Docker.
    helm version        # para confirmar a instalação do Helm.
    kubectl version     # para verificar se o Kubernetes está configurado.
    minikube version    # para confirmar a instalação do Minikube.
    postman             # abra o Postman para verificar se ele está funcionando corretamente.
    ```

2. **Configure o Kubernetes Dashboard**:
   - Siga a [documentação do Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/) para configurá-lo e verificar o acesso ao ambiente do cluster.

---

**ATENÇÃO** -> PRECISA DETALHAR MELHOR ESSE TRECHO DO TRABALHO.

---

### 1.2. Limpeza do Ambiente (Opcional)

Este passo pode ser importante para garantir que o ambiente esteja limpo de configurações e dados antigos, evitando problemas de conflito.

---

#### Limpeza do Persistent Volume Claim (PVC)

1. **Verifique os PVCs Existentes**
Primeiro, liste os PVCs no namespace onde está rodando a sua aplicação. Se você estiver usando o namespace padrão, pode deixar o parâmetro `-n`.

```bash
kubectl get pvc -n <seu-namespace>
```

> **Nota**: Substitua `<seu-namespace>` pelo namespace correto (ex.: `default`).

Isso mostrará uma lista dos PVCs, onde você pode identificar qual PVC é o responsável pelo armazenamento da sua aplicação.

2. **Exclua o PVC**
Com o nome do PVC em mãos, exclua-o usando o comando abaixo:

```bash
kubectl delete pvc <nome-do-pvc> -n <seu-namespace>
```

> **Nota**: Substitua `<nome-do-pvc>` pelo nome do PVC que você deseja remover.

3. **Verifique se o PVC e o PV Foram Removidos**
Confirme que o PVC foi removido e que o Persistent Volume (PV) associado também foi desalocado. Liste novamente para garantir que eles não estão mais presentes:

```bash
kubectl get pvc -n <seu-namespace>
kubectl get pv
```

O PV associado ao PVC deve ter sido removido automaticamente (ou estar marcado como `Released` ou `Available` se não for removido automaticamente).

4. **(Opcional) Forçar Exclusão do PV**
Se o PV associado não for removido automaticamente e estiver marcado como `Released`, você pode excluí-lo manualmente:

```bash
kubectl delete pv <nome-do-pv>
```

Isso deve garantir que o armazenamento persistente seja completamente removido.

---

#### Limpeza do Helm

1. **Desinstalar *charts* e liberar recursos**:
    ```bash
    helm uninstall <nome_do_release>

2. **Remover Releases do Helm**:
   ```bash
   helm list --all-namespaces -q | xargs -L1 helm uninstall
   ```

3. **Remover Repositórios do Helm**:
   ```bash
   helm repo remove $(helm repo list -o json | jq -r '.[].name')
   ```

4. **Remover Todas as Releases e Repositórios do Helm**:
  ```bash
  helm ls --all --short | xargs -n 1 helm delete
  helm repo list --short | xargs -n 1 helm repo remove
  rm -rf ~/.cache/helm ~/.config/helm ~/.local/share/helm/plugins
  ```

---

#### Limpeza do Kubernetes e Minikube

1. **Inicie o Minikube Temporariamente** (se necessário para acesso às configurações):
   ```bash
   minikube start # minikube start --driver=docker (opcional)
   ```

2. **Remova Contextos e Namespaces no Kubernetes** (enquanto o Minikube estiver ativo):
   - **Apagar Contexto do Minikube**:
     ```bash
     kubectl config delete-context minikube
     kubectl config unset current-context
     ```
   - **Remover Namespaces Personalizados**:
     ```bash
     kubectl delete namespaces $(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}' | tr ' ' '\n' | grep -vE 'kube|default')
     ```

3. **Remover todos os recursos do cluster**:
    ```bash
    kubectl delete all --all
    ```

4. **Parar e Apagar o Cluster do Minikube**:
   ```bash
   minikube stop
   minikube delete --all
   ```

---

#### Limpeza do Docker

1. **Parar e Remover Contêineres**:
   ```bash
   docker stop $(docker ps -aq)
   docker rm $(docker ps -aq)
   ```
  - **Remover contêineres parados**:
      ```bash
      docker container prune
      ```

2. **Remover Imagens**:
   ```bash
   docker rmi $(docker images -q) -f
   ```

  - **Remover imagens não utilizadas**:
      ```bash
      docker image prune -a
      ```

3. **Remover Volumes**:
   ```bash
   docker volume rm $(docker volume ls -q)
   ```

  - **Remover volumes não utilizados**:
      ```bash
      docker volume prune
      ```

4. **Remover Redes Criadas pelo Usuário**:
   ```bash
   docker network prune -f
   ```

---

### 1.3. Iniciando o Ambiente

#### 1.3.1. Iniciar o Docker

1. **Verifique se o Docker está instalado e em execução**:
  - Para Linux:
    ```bash
    sudo systemctl start docker # Para sistemas Linux com systemd
    ```
  - Para Windows:
    - Abra o **Gerenciador de Tarefas**.
    - Encontre o serviço **Docker Desktop**.
    - Clique com o botão direito e selecione **Reiniciar**.

#### 1.3.2. Iniciar o Minikube

1. **Verifique se o Minikube está instalado**:
   ```bash
   minikube version
   ```

2. **Inicie o Minikube**:
   ```bash
   minikube start
   ```

3. **Confirme se o cluster está ativo (Opcional)**:
   ```bash
   kubectl cluster-info
   ```

4. **Configure o Docker para usar o Minikube**:
  ```bash
  eval $(minikube docker-env)
  ```

#### 1.3.3. Iniciar o Kubernetes Dashboard (Opcional)

1. **Inicie o Dashboard do Kubernetes**:
   ```bash
   minikube dashboard
   ```

2. **Acesse o Dashboard**: O comando abrirá o dashboard no navegador.

#### 1.3.4. Baixar o Programa do GitHub

1. **Baixar o programa OrchestrateOps**:
   - Acesse o link do repositório no GitHub: [https://github.com/felipe-fsm/OrchestrateOps.git](https://github.com/felipe-fsm/OrchestrateOps.git) e clique em **Code > Download ZIP** para baixar o arquivo compactado.

2. **Clonar o repositório via HTTPS**:
   - Como alternativa, você pode clonar o repositório diretamente com o comando:
     ```bash
     git clone https://github.com/felipe-fsm/OrchestrateOps.git
     ```

#### 1.3.5. Instalar a Aplicação OrchestrateOps via Helm

1. **Navegue até o Diretório do Chart**:
   - Acesse o diretório `OrchestrateOps/helm`, onde o chart do Helm da aplicação está localizado:
     ```bash
     cd OrchestrateOps/helm
     ```

2. **Instale o Chart do Helm**:
   - Use o comando `helm install` apontando para o diretório do chart. Substitua `<nome_do_release>` pelo nome desejado para a instalação:
     ```bash
     helm install <nome_do_release> ./orchestrateops-chart
     ```
   - Exemplo:
     ```bash
     helm install orchestrateops-release ./orchestrateops-chart
     ```

3. **Verifique a Instalação**:
   - Confirme se a aplicação foi instalada e os recursos estão ativos:
     ```bash
     kubectl get pods
     kubectl get services
     ```

   - **Verifique os PVCs** (Persistent Volume Claims):
     ```bash
     kubectl get pvc
     ```

   - **Verifique os PVs** (Persistent Volumes):
     ```bash
     kubectl get pv
     ```

4. **Alternativa para Acessar o Serviço no Minikube com QEMU**:

    1. **Obtenha o NodePort do Serviço**:
    - Verifique o NodePort (a porta externa) que o Kubernetes atribuiu ao serviço:
        ```bash
        kubectl get services
        ```
    - Procure a linha correspondente ao serviço `orchestrateops-release` e anote a porta externa na coluna `PORT(S)` (geralmente no formato `PORT:NodePort`).

    2. **Recupere o IP do Minikube**:
    - Pegue o IP do Minikube para acessar o serviço externamente:
        ```bash
        minikube ip
        ```

    3. **Acesse o Serviço**:
    - No seu navegador ou terminal, acesse o serviço usando o IP do Minikube e o NodePort obtido. O formato será:
        ```
        http://<minikube_ip>:<node_port>
        ```
    - Exemplo:
        ```bash
        http://192.168.99.100:30000
        ```

5. **Configurar Port Forwarding para Acesso Local**:
   - Verifique os pods em execução:
     ```bash
     kubectl get pods
     ```

   - Configure o port forwarding:
     ```bash
     kubectl port-forward pod/<nome-do-pod> 8080:80

---

**ATENÇÃO - Em desenvolvimento - Início da Seção**

### 1.4. Passo a Passo para Iniciar o Ambiente no Laboratório de Informática

Para utilizar a aplicação **OrchestrateOps** em um laboratório de informática, há alguns fatores importantes a considerar, como os tipos de usuários, onde a aplicação deve ser instalada e o gerenciamento de volumes persistentes (PVCs e PVs). Vamos detalhar cada aspecto:

### 1. Papéis de Usuários e Acesso

Em um laboratório de informática, geralmente existem dois papéis principais de usuários:

- **Administrador do Laboratório**: Responsável pela configuração inicial, instalação e manutenção da aplicação no ambiente compartilhado.
- **Usuários Finais (Estudantes/Alunos)**: Utilizam a aplicação para realizar operações CRUD (criação, leitura, atualização e deleção) sem necessidade de configurar a infraestrutura.

Esses papéis indicam que o **administrador** deve configurar a aplicação centralmente, enquanto os **usuários finais** devem apenas acessar a aplicação, preferencialmente por um ponto centralizado.

### 2. Instalação Centralizada no Cluster

Para simplificar o acesso e evitar configurações repetidas, a aplicação **OrchestrateOps** deve ser instalada em um cluster centralizado (por exemplo, usando Minikube ou um cluster Kubernetes de maior porte) acessível a todos os usuários.

- **Instalação no Servidor Central**: A aplicação deve ser instalada em uma única máquina no laboratório, que servirá como o **nó do cluster**.
- **Acesso Remoto via Terminal**: Os usuários podem acessar a aplicação a partir de suas máquinas usando `kubectl` ou um endereço IP exposto no servidor central. Eles podem usar comandos `curl` ou interfaces como Postman, sem a necessidade de instalar o cluster localmente.

### 3. Direcionamento e Configuração dos PVCs e PVs

Para que os dados sejam armazenados de forma persistente e acessível a todos os usuários, o administrador deve configurar volumes persistentes:

- **Configurar PVC e PV no Cluster Central**: Ao instalar a aplicação, o administrador deve configurar Persistent Volume Claims (PVCs) e Persistent Volumes (PVs) para armazenar os dados de maneira compartilhada.
- **Acesso Compartilhado**: Todos os usuários acessarão os dados do mesmo PVC/PV configurado, garantindo persistência e consistência dos dados.
  
Para garantir que o armazenamento esteja acessível a todos os usuários:

1. **Criar e Vincular PVs e PVCs**: No arquivo Helm ou YAML de implantação, configurar PVs e PVCs para uso compartilhado.

2. **Montar o PVC na Aplicação**: Certifique-se de que o PVC está montado no pod onde a aplicação roda, permitindo que todos os dados sejam salvos de forma persistente.

### 4. Acesso e Uso pelos Usuários Finais

Uma vez configurada a aplicação no servidor central com o PVC e PV para persistência:

- **Redirecionamento de Porta para Acesso Externo**: Configure o Kubernetes ou o Minikube para expor a aplicação por meio de um NodePort ou um Ingress, facilitando o acesso aos usuários finais.

- **Passo a Passo para Usuários Finais**:
  1. Acessar o endereço IP do servidor ou a URL configurada.
  2. Realizar operações na aplicação via Postman, curl, ou qualquer cliente HTTP.

Esses passos simplificam o uso para os alunos e mantêm a aplicação centralizada e gerenciável pelo administrador do laboratório.

**ATENÇÃO - Em desenvolvimento - Término da Seção**

---