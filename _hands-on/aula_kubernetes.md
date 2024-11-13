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

## Tecnologias Utilizadas para a Aula

### Curl
**Curl** é uma ferramenta de linha de comando que permite fazer requisições HTTP e outras requisições de rede de maneira simples e direta. Ele é amplamente utilizado para interagir com APIs, testar endpoints, e enviar dados em diversos formatos, como JSON, XML ou formulários. Com Curl, é possível simular requisições GET, POST, PUT, DELETE e outras, ideal para depurar e testar a comunicação com APIs RESTful ou serviços web.
- [Documentação Curl](https://curl.se/docs/)

---

### Docker
**Docker** é uma plataforma que facilita o empacotamento, o desenvolvimento e a execução de aplicações em containers. Containers são unidades leves que contêm o código da aplicação, suas dependências e o ambiente necessário, permitindo que a aplicação rode de maneira consistente em qualquer máquina. Com Docker, desenvolvedores conseguem criar, compartilhar e distribuir containers facilmente, garantindo que o software funcione da mesma maneira em diferentes ambientes (desenvolvimento, teste e produção).
- [Documentação Docker](https://docs.docker.com/)

---

### Helm
**Helm** é um gerenciador de pacotes para Kubernetes, facilitando o processo de instalação e gerenciamento de aplicações complexas em clusters. Ele utiliza *charts*, pacotes que contêm templates YAML e configurações para o Kubernetes, permitindo implantar e atualizar aplicações com facilidade. Helm simplifica a gestão de dependências e configurações, sendo especialmente útil para ambientes com múltiplas instâncias ou configurações complexas.
- [Documentação Helm](https://helm.sh/docs/)

---

### Kind (Kubernetes in Docker)
**Kind** é uma ferramenta que permite rodar clusters Kubernetes localmente utilizando containers Docker. É ideal para ambientes de desenvolvimento e testes, permitindo que desenvolvedores criem um cluster Kubernetes de múltiplos nós diretamente em seus computadores ou em ambientes de CI/CD. Kind é prático para experimentar e testar mudanças sem a necessidade de um cluster real em produção.
- [Documentação Kind](https://kind.sigs.k8s.io/docs/)

---

### Kubernetes
**Kubernetes** é um sistema de orquestração de containers que gerencia o deployment, o escalonamento e o gerenciamento de aplicações em containers. Ele distribui e coordena containers em um cluster de máquinas, automatizando tarefas complexas como balanceamento de carga, resiliência a falhas, escalabilidade, e atualizações sem tempo de inatividade. Kubernetes se destaca pela sua capacidade de adaptar a infraestrutura de acordo com a demanda e otimizar o uso de recursos.
- [Documentação Kubernetes](https://kubernetes.io/docs/)

---

### Kubernetes Dashboard
**Kubernetes Dashboard** é uma interface gráfica que permite aos usuários visualizar e gerenciar recursos em um cluster Kubernetes. Ele proporciona uma visão detalhada de pods, serviços, deployments e outras métricas do cluster, facilitando a administração e o monitoramento do ambiente Kubernetes. É útil para acompanhar o status dos recursos e resolver problemas com uma interface visual intuitiva.
- [Documentação Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

---

### Minikube
**Minikube** é uma ferramenta que permite rodar um cluster Kubernetes localmente, ideal para ambientes de desenvolvimento e teste. Ele cria um ambiente Kubernetes de nó único (single-node) em uma máquina local, permitindo que desenvolvedores explorem e testem o Kubernetes em uma configuração simplificada. Minikube é especialmente útil para experimentar e desenvolver localmente antes de implementar em um cluster em produção.
- [Documentação Minikube](https://minikube.sigs.k8s.io/docs/)

---

### Postman
**Postman** é uma ferramenta que facilita o desenvolvimento, teste e documentação de APIs. Ela permite que desenvolvedores enviem requisições HTTP, configurem parâmetros, visualizem respostas e gerem scripts automatizados para testar APIs RESTful. Postman é popular entre desenvolvedores que precisam simular, depurar e automatizar o teste de APIs, e também facilita a colaboração em equipes, com a criação de coleções de requisições compartilháveis.
- [Documentação Postman](https://learning.postman.com/docs/getting-started/introduction/)

---

Essas ferramentas formam uma stack poderosa para o desenvolvimento de software moderno, proporcionando desde a criação e o empacotamento de containers até a orquestração e o monitoramento de aplicações distribuídas.

---

## Etapas da Aula

Durante esta aula, exploraremos o Kubernetes em detalhes, entenderemos seu funcionamento e faremos exercícios práticos para aplicá-lo.

### 1. Configuração do Ambiente

#### 1.1. Requisitos e Dependências

##### Verificação dos Requisitos e Dependências

1. **Verifique se todos os requisitos estão instalados**:
  
```bash
curl --version      # para confirmar a instalação do Curl.
docker --version    # para confirmar a instalação do Docker.
helm version        # para confirmar a instalação do Helm.
kind version        # para confirmar a instalação do Kind.
kubectl version     # para verificar se o Kubernetes está configurado.
```
    
  - Abra o Postman para verificar se ele está funcionando corretamente.

2. **Configure o Kubernetes Dashboard**:
  
  - Siga a [documentação do Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/) para configurá-lo e verificar o acesso ao ambiente do cluster.

---

### 1.2. Baixar a Aplicação OrchestrateOps do GitHub

1. **Baixar o programa OrchestrateOps**:
   - Acesse o link do repositório no GitHub: [https://github.com/felipe-fsm/OrchestrateOps.git](https://github.com/felipe-fsm/OrchestrateOps.git) e clique em **Code > Download ZIP** para baixar o arquivo compactado.

2. **Clonar o repositório via HTTPS**:
   - Como alternativa, você pode clonar o repositório diretamente com o comando:
     ```bash
     git clone https://github.com/felipe-fsm/OrchestrateOps.git
     ```

### 2. Limpeza do Ambiente (Opcional)

Este passo pode ser importante para garantir que o ambiente esteja limpo de configurações e dados antigos, evitando problemas de conflito.

Observação: é necessário que do Docker esteja ativo e que exista um cluster Kind iniciado para realizar a limpeza do Helm e do Kubernetes.

Aqui está a explicação detalhada de cada comando:

---

#### 2.1. **Remover todos os releases do Helm em todos os namespaces**

```bash
helm list --all-namespaces -q | while read release; do
  namespace=$(helm list --all-namespaces | grep "$release" | awk '{print $2}')
  helm uninstall "$release" --namespace "$namespace"
done
```

Este comando faz o seguinte:

- **`helm list --all-namespaces -q`**: lista todos os releases do Helm em todos os namespaces, mostrando apenas os nomes dos releases (`-q` suprime outros detalhes, exibindo apenas o nome do release).
- **`while read release; do ... done`**: para cada release listado, o loop `while` executa uma sequência de comandos.
  - **`namespace=$(helm list --all-namespaces | grep "$release" | awk '{print $2}')`**: obtém o namespace do release específico:
    - **`helm list --all-namespaces | grep "$release"`**: encontra a linha completa do release atual.
    - **`awk '{print $2}'`**: extrai o segundo campo dessa linha (que é o namespace).
  - **`helm uninstall "$release" --namespace "$namespace"`**: desinstala o release do Helm com o nome `$release` no namespace `$namespace`.

**Resultado**: Este comando remove todos os releases do Helm em todos os namespaces no cluster Kubernetes.

---

#### 2.2. **Deletar todos os recursos do Kubernetes em todos os namespaces**

```bash
kubectl delete all --all --all-namespaces
```

Este comando utiliza `kubectl` (ferramenta de linha de comando para Kubernetes) para:

- **`delete all --all --all-namespaces`**: excluir todos os recursos que correspondem ao tipo `all` (ou seja, todos os tipos de recursos padrão como pods, services, deployments, etc.) em todos os namespaces do cluster (`--all-namespaces`).

**Resultado**: Remove todos os recursos do Kubernetes no cluster, independentemente do namespace.

---

#### 2.3. **Excluir todos os clusters do Kind**

```bash
for cluster in $(kind get clusters); do
    kind delete cluster --name $cluster
done
```

Este comando realiza as seguintes ações:

- **`kind get clusters`**: lista todos os clusters gerenciados pela ferramenta Kind.
- **`for cluster in $(kind get clusters); do ... done`**: percorre cada cluster listado e executa o comando dentro do loop.
  - **`kind delete cluster --name $cluster`**: exclui o cluster com o nome especificado em `$cluster`.

**Resultado**: Remove todos os clusters do Kind (Kubernetes in Docker) do ambiente local.

---

#### 2.4. **Limpeza total do Docker**

```bash
docker system prune --all --volumes --force
```

Este comando faz uma limpeza abrangente no Docker:

- **`docker system prune`**: remove todos os dados não utilizados do Docker, como containers parados, imagens sem uso, volumes e redes não referenciadas.
  - **`--all`**: remove todas as imagens, incluindo as que não estão associadas a containers.
  - **`--volumes`**: remove todos os volumes do Docker.
  - **`--force`**: evita a necessidade de confirmação (força a execução).

**Resultado**: Libera espaço no sistema, removendo todos os recursos ociosos do Docker (imagens, volumes, redes e containers).

---

#### 2.5. **Parar o Docker e o socket do Docker**

```bash
sudo systemctl stop docker docker.socket
```

Este comando usa `systemctl` para parar os serviços do Docker:

- **`sudo systemctl stop docker`**: para o serviço principal do Docker.
- **`docker.socket`**: o socket do Docker, usado para receber conexões.

**Resultado**: Para completamente o serviço do Docker, impedindo a execução de containers e o gerenciamento dos recursos pelo Docker no sistema.

--- 

Esses comandos juntos permitem uma "limpeza completa" de um ambiente Kubernetes local em um ambiente Docker, removendo todos os recursos de clusters, Helm e Docker e finalizando o serviço do Docker.

---

### 3. Iniciando o Ambiente

Aqui estão as instruções revisadas para iniciar o Docker, criar o cluster Kind e instalar o release Helm, considerando as diferenças de execução entre Linux e Windows e instruções para navegar até os diretórios apropriados.

---

#### 3.1. **Iniciar o Docker**

##### No Linux:
Para iniciar o Docker, use o comando `systemctl` com permissões de superusuário (sudo).

```bash
sudo systemctl start docker
```

Este comando inicia o serviço Docker, permitindo o gerenciamento de containers e recursos associados.

##### No Windows:
No Windows, o Docker geralmente é iniciado através do Docker Desktop. Siga estes passos:

1. Abra o aplicativo **Docker Desktop**.
2. Verifique se ele está em execução (o ícone do Docker deve aparecer na barra de tarefas).
3. Se o Docker não estiver iniciado automaticamente, clique no ícone para abrir o Docker Desktop e iniciar o serviço.

**Resultado esperado**: O Docker estará em execução no sistema, permitindo a criação de containers e clusters.

---

#### 3.2. **Criar um cluster Kind**

Para criar o cluster Kind, você precisará usar um arquivo de configuração que define os detalhes do cluster.

1. Navegue até a pasta onde o arquivo de configuração está localizado.

2. Execute o comando abaixo para criar o cluster, utilizando o nome do arquivo de configuração local:

   ```bash
   kind create cluster --name <nome-do-cluster> --config <nome-do-arquivo>.yaml
   ```

---

  No exemplo, o arquivo `kind-cluster-config.yaml` está em:

    ```bash
    cd /home/felipe/GitHub/OrchestrateOps/kind/
    ```

  E o comando para criar o cluster utilizando o nome do arquivo de configuração local é:

    ```bash
    kind create cluster --name orchestrateops-cluster --config kind-cluster-config.yaml
   ```

  Esse comando cria um cluster chamado `orchestrateops-cluster` com a configuração especificada em `kind-cluster-config.yaml`.

  **Resultado esperado**: O Kind criará um cluster Kubernetes utilizando o Docker, de acordo com as especificações do arquivo `kind-cluster-config.yaml`.

---

#### 3.3. **Instalar o release do Helm**

Para instalar um release do Helm no cluster Kind, você precisa acessar o diretório onde o chart do Helm está localizado. O chart é o pacote que contém os templates e configurações necessários para implantar a aplicação no Kubernetes.

1. Navegue até a pasta que contém o chart Helm.

2. Execute o comando abaixo para instalar o release:

   ```bash
   helm install <nome-da-release> .
   ```

  No exemplo, o chart do Helm está em:

    ```bash
    cd /home/felipe/GitHub/OrchestrateOps/helm/orchestrateops-chart/
    ```

  E o comando para instalar o release é:

    ```bash
    helm install orchestrateops-release .
    ```

  Aqui, `orchestrateops-release` é o nome do release, e o `.` indica que o chart está no diretório atual.


  **Resultado esperado**: O Helm instalará o release `orchestrateops-release` no cluster Kubernetes utilizando o chart localizado na pasta `orchestrateops-chart`. Isso criará os recursos necessários (como deployments e serviços) para a aplicação no cluster Kind.

---

Essas instruções orientam o usuário a iniciar o Docker, navegar para os diretórios apropriados e executar os comandos necessários para configurar o cluster e instalar a aplicação.

---

### 4. Comandos úteis para Kubernetes

Aqui está uma seleção dos comandos Kubernetes mais utilizados na prática para verificar o estado de recursos em um cluster, junto com uma breve explicação do motivo de cada um:

#### 1. **kubectl get pods -A**
   - **Uso**: Verifica todos os pods em todos os namespaces.
   - **Motivo**: É um dos comandos mais usados para monitorar o estado dos pods, verificando se estão `Running`, `Pending`, `CrashLoopBackOff`, entre outros status.

#### 2. **kubectl get services -A**
   - **Uso**: Lista todos os serviços em todos os namespaces.
   - **Motivo**: Útil para monitorar quais serviços estão em execução e confirmar se as conexões entre pods e outros recursos estão funcionando conforme esperado.

#### 3. **kubectl get pvc -A** e **kubectl get pv**
   - **Uso**: Exibe todas as `PersistentVolumeClaims` (PVC) em todos os namespaces e todos os `PersistentVolumes` (PV) no cluster.
   - **Motivo**: Esses comandos são importantes para monitorar o armazenamento, especialmente em clusters que usam volumes persistentes para dados de aplicativos.

#### 4. **kubectl get nodes -o wide**
   - **Uso**: Lista todos os nós do cluster com detalhes adicionais, como IP, status e função.
   - **Motivo**: Fundamental para verificar o estado dos nós, entender a distribuição de pods e monitorar a saúde geral do cluster.

#### 5. **kubectl get deployments -A**
   - **Uso**: Lista todos os deployments em todos os namespaces.
   - **Motivo**: Útil para confirmar o estado das réplicas de aplicativos e garantir que os deployments estejam atualizados e com o número correto de réplicas.

#### 6. **kubectl get replicasets -A**
   - **Uso**: Mostra todas as ReplicaSets em todos os namespaces.
   - **Motivo**: Importante para verificar o estado dos ReplicaSets, que gerenciam a quantidade de réplicas dos pods associados a um deployment.

#### 7. **kubectl get namespaces**
   - **Uso**: Lista todos os namespaces no cluster.
   - **Motivo**: Útil para ter uma visão geral de todos os ambientes no cluster (cada namespace pode representar um ambiente ou aplicação).

#### 8. **kubectl get ingresses -A**
   - **Uso**: Lista todos os ingressos em todos os namespaces.
   - **Motivo**: Essencial para monitorar as regras de roteamento de tráfego externo para os serviços dentro do cluster.

#### 9. **kubectl get configmaps -A** e **kubectl get secrets -A**
   - **Uso**: Mostra todos os ConfigMaps e Secrets em todos os namespaces.
   - **Motivo**: Importante para verificar e gerenciar configurações de aplicativos (ConfigMaps) e informações sensíveis (Secrets).

#### 10. **kubectl get events -A**
   - **Uso**: Lista todos os eventos em todos os namespaces.
   - **Motivo**: Muito útil para diagnóstico, pois mostra eventos como falhas de criação de pods, problemas de rede e alertas de recursos.

---

#### Comandos Adicionais Menos Utilizados

Os comandos a seguir são usados em cenários mais específicos e não são necessariamente consultados com frequência:

- **kubectl get statefulsets -A**: Útil quando se trabalha com aplicações que requerem armazenamento persistente e gerenciamento de estado.
- **kubectl get daemonsets -A**: Verifica daemonsets, que garantem que certos pods estejam em execução em todos os nós. Importante em casos específicos de infraestrutura.
- **kubectl get jobs -A** e **kubectl get cronjobs -A**: Consultados quando se trabalha com tarefas de processamento em lotes.
- **kubectl get networkpolicies -A**: Necessário para monitorar políticas de rede aplicadas entre pods, mas menos comum em clusters pequenos.
- **kubectl get resourcequotas -A** e **kubectl get limitranges -A**: São úteis para monitorar quotas e limites de recursos nos namespaces, mas geralmente usados em clusters com controle rígido de uso de recursos.
- **kubectl get hpa -A**: Lista as Horizontal Pod Autoscalers, usadas para escalar automaticamente pods com base no uso de recursos.

#### Resumo dos Comandos Mais Utilizados
Para monitoramento regular, os comandos mais úteis geralmente são:

1. `kubectl get pods -A`
2. `kubectl get services -A`
3. `kubectl get pvc -A` e `kubectl get pv`
4. `kubectl get nodes -o wide`
5. `kubectl get deployments -A`
6. `kubectl get replicasets -A`
7. `kubectl get namespaces`
8. `kubectl get ingresses -A`
9. `kubectl get configmaps -A` e `kubectl get secrets -A`
10. `kubectl get events -A`

Esses comandos oferecem uma visão completa e rápida do status e da saúde do cluster, atendendo a maioria das necessidades de monitoramento e diagnóstico no dia a dia.

---

### 5. Verificando a Instalação da Aplicação

#### 5.1. Verificando o Release

   ```bash
   kubectl get pods
   kubectl get nodes
   kubectl get pv
   kubectl get pvc
   kubectl get services
   ```

---

### 6. Testes e Simulações

#### 6.1. Teste de Conectividade via Solicitação `GET` no Postman

Este guia mostra como realizar uma solicitação `GET` no Postman para verificar a conectividade com o endpoint da aplicação. A solicitação `GET` ao endereço `http://localhost:30010` ajuda a confirmar que o serviço está em execução e acessível.

1. **Abra o Postman** e selecione o método **GET** no canto superior esquerdo.

2. **Digite o endereço do endpoint**:

   ```
   http://localhost:30010
   ```

   Esse é o URL base da aplicação, e uma solicitação `GET` aqui deve retornar uma resposta indicando que o servidor está ativo.

3. **Enviar a solicitação**:

   - Clique em **Send** para enviar a solicitação `GET`.

4. **Verifique a Resposta**:

   Após enviar a solicitação, observe o painel de resposta no Postman. Uma resposta bem-sucedida pode ser algo como:

   ```json
   {
      "message": "Bem-vindo ao OrchestrateOps"
   }
   ```

   A mensagem de retorno pode variar conforme a configuração da aplicação, mas qualquer resposta de sucesso indica que o servidor está acessível em `localhost:30010`.

##### Exemplo de Resposta Esperada

Se o servidor estiver ativo, você deve receber uma resposta com um status de sucesso (`200 OK`) e uma mensagem semelhante a:

```json
{
    "message": "Bem-vindo ao OrchestrateOps"
}
```

Essa resposta confirma que a aplicação está em execução e pronta para receber outras solicitações.

---

#### 6.2. Teste de Criação via Solicitação `POST` no Postman

Este guia mostra como enviar uma solicitação `POST` no Postman para criar uma nova solicitação no endpoint da aplicação. Usaremos o endereço `http://localhost:30010/solicitacoes/`, com um corpo (`body`) em formato JSON contendo os dados da solicitação.

1. **Abra o Postman** e selecione o método **POST** no canto superior esquerdo.

2. **Digite o endereço do endpoint**:

   ```
   http://localhost:30010/solicitacoes/
   ```

   Esse é o URL para o endpoint onde a nova solicitação será criada.

3. **Configurar o Body da Solicitação**:

   - Clique na aba **Body**.
   - Selecione **raw** para o tipo de dados.
   - No menu suspenso à direita de `raw`, escolha **JSON** (para garantir que o Postman envie o body como JSON).

4. **Inserir os dados da solicitação**:

   No campo `Body`, copie e cole o seguinte JSON, ajustando os valores conforme necessário:

   ```json
      {
         "id": 1,
         "setor": "Setor A",
         "solicitante": "Solicitante A",
         "produto": "Produto A",
         "quantidade": 5,
         "status": "pendente"
      }
   ```

   - **setor**: Nome do setor solicitante.
   - **solicitante**: Nome da pessoa que está fazendo a solicitação.
   - **produto**: Nome do produto solicitado.
   - **quantidade**: Quantidade do produto solicitado.
   - **status**: Status inicial da solicitação (por exemplo, "pendente").

5. **Enviar a solicitação**:

   - Clique em **Send** para enviar a solicitação.
   - Verifique a resposta retornada no painel de respostas do Postman para confirmar que a solicitação foi criada com sucesso.

##### Exemplo de Resposta Esperada

Se tudo estiver correto, o servidor deve responder com uma confirmação e os dados da solicitação criada, algo assim:

```json
   {
      "id": 1,
      "setor": "Setor A",
      "solicitante": "Solicitante A",
      "produto": "Produto A",
      "quantidade": 5,
      "status": "pendente"
   }
```

Essa resposta indica que a solicitação foi criada e armazenada com sucesso no sistema, juntamente com um identificador único (`id`), que permite consultar ou atualizar essa solicitação no futuro.

---

Esse procedimento facilita o teste do endpoint para criar uma nova solicitação na aplicação usando o Postman.

Aqui estão os textos em Markdown para os testes `GET` de listagem de todas as solicitações e de uma solicitação específica pelo `id`.

---

#### 6.3. Teste de Leitura de Todas as Solicitações via Solicitação `GET` no Postman

Este guia mostra como enviar uma solicitação `GET` no Postman para listar todas as solicitações no endpoint da aplicação. Usaremos o endereço `http://localhost:30010/solicitacoes/` para obter a lista completa de solicitações registradas.

1. **Abra o Postman** e selecione o método **GET** no canto superior esquerdo.

2. **Digite o endereço do endpoint**:

   ```
   http://localhost:30010/solicitacoes/
   ```

   Esse é o URL que retorna a lista de todas as solicitações armazenadas na aplicação.

3. **Enviar a solicitação**:

   - Clique em **Send** para enviar a solicitação `GET`.

4. **Verifique a Resposta**:

   Após enviar a solicitação, observe o painel de resposta no Postman. Se houver solicitações registradas, você deve ver uma lista com todas elas, como o exemplo a seguir:

   ```json
   [
       {
           "id": 1,
           "setor": "Setor A",
           "solicitante": "Solicitante A",
           "produto": "Produto A",
           "quantidade": 5,
           "status": "pendente"
       },
       {
           "id": 2,
           "setor": "Setor B",
           "solicitante": "Solicitante B",
           "produto": "Produto B",
           "quantidade": 3,
           "status": "pendente"
       }
   ]
   ```

Essa resposta indica que a aplicação retornou todas as solicitações cadastradas, cada uma com um `id` e os detalhes correspondentes.

---

#### 6.4. Teste de Leitura de uma Solicitação Específica via Solicitação `GET` no Postman

Este guia mostra como enviar uma solicitação `GET` no Postman para consultar uma solicitação específica pelo `id`. Usaremos o endereço `http://localhost:30010/solicitacoes/1` para obter os detalhes da solicitação com `id` igual a 1.

1. **Abra o Postman** e selecione o método **GET** no canto superior esquerdo.

2. **Digite o endereço do endpoint**:

   ```
   http://localhost:30010/solicitacoes/1
   ```

   Esse é o URL que retorna as informações da solicitação com `id` igual a 1.

3. **Enviar a solicitação**:

   - Clique em **Send** para enviar a solicitação `GET`.

4. **Verifique a Resposta**:

   Após enviar a solicitação, observe o painel de resposta no Postman. Se a solicitação com o `id` especificado existir, você deve ver uma resposta com os dados dessa solicitação específica, como no exemplo abaixo:

   ```json
   {
       "id": 1,
       "setor": "Setor A",
       "solicitante": "Solicitante A",
       "produto": "Produto A",
       "quantidade": 5,
       "status": "pendente"
   }
   ```

Essa resposta indica que a aplicação retornou as informações da solicitação com `id` 1, exibindo os dados específicos como setor, solicitante, produto, quantidade e status.

---

#### 6.5. Teste de Atualização de uma Solicitação via Solicitação `PUT` no Postman

Este guia mostra como enviar uma solicitação `PUT` no Postman para atualizar os dados de uma solicitação existente. Usaremos o endereço `http://localhost:30010/solicitacoes/1`, onde `1` representa o `id` da solicitação que queremos atualizar.

1. **Abra o Postman** e selecione o método **PUT** no canto superior esquerdo.

2. **Digite o endereço do endpoint**:

   ```
   http://localhost:30010/solicitacoes/1
   ```

   Esse é o URL para atualizar a solicitação com `id` igual a 1.

3. **Configurar o Body da Solicitação**:

   - Clique na aba **Body**.
   - Selecione **raw** para o tipo de dados.
   - No menu suspenso à direita de `raw`, escolha **JSON**.

4. **Inserir os dados atualizados da solicitação**:

   No campo `Body`, copie e cole o JSON com as informações atualizadas da solicitação, ajustando os valores conforme necessário:

   ```json
   {
       "setor": "Setor Atualizado",
       "solicitante": "Solicitante Atualizado",
       "produto": "Produto Atualizado",
       "quantidade": 15,
       "status": "em processamento"
   }
   ```

   - **setor**: Nome do setor atualizado.
   - **solicitante**: Nome do solicitante atualizado.
   - **produto**: Nome do produto atualizado.
   - **quantidade**: Quantidade do produto atualizada.
   - **status**: Novo status da solicitação (por exemplo, "em processamento").

5. **Enviar a solicitação**:

   - Clique em **Send** para enviar a solicitação.
   - Verifique a resposta no Postman para confirmar que a solicitação foi atualizada com sucesso.

##### Exemplo de Resposta Esperada

Se a atualização for bem-sucedida, a resposta pode ser similar a esta, indicando que os dados foram atualizados:

```json
{
    "id": 1,
    "setor": "Setor Atualizado",
    "solicitante": "Solicitante Atualizado",
    "produto": "Produto Atualizado",
    "quantidade": 15,
    "status": "em processamento"
}
```

Essa resposta confirma que a solicitação foi atualizada no sistema com os novos valores fornecidos.

---

#### 6.6. Teste de Exclusão de uma Solicitação via Solicitação `DELETE` no Postman

Este guia mostra como enviar uma solicitação `DELETE` no Postman para excluir uma solicitação existente. Usaremos o endereço `http://localhost:30010/solicitacoes/1`, onde `1` representa o `id` da solicitação que queremos excluir.

1. **Abra o Postman** e selecione o método **DELETE** no canto superior esquerdo.

2. **Digite o endereço do endpoint**:

   ```
   http://localhost:30010/solicitacoes/1
   ```

   Esse é o URL para excluir a solicitação com `id` igual a 1.

3. **Enviar a solicitação**:

   - Clique em **Send** para enviar a solicitação `DELETE`.

4. **Verifique a Resposta**:

   Após enviar a solicitação, observe o painel de resposta no Postman. Uma resposta de sucesso pode ser algo assim:

   ```json
   {
       "message": "Solicitação excluída com sucesso",
       "id": 1
   }
   ```

   Esse retorno confirma que a solicitação com `id` 1 foi removida do sistema.

---

Aqui está o texto em Markdown para documentar um teste de persistência de dados, seguido de uma explicação do que ocorre durante o processo.

---

#### 6.7. Teste de Persistência de Dados

Este guia mostra como realizar um teste de persistência de dados em uma aplicação Kubernetes para garantir que os dados são mantidos mesmo após a remoção e reinstalação da aplicação.

1. **Crie uma Solicitação Inicial para Testar a Persistência**:
   - Usando o Postman ou `curl`, envie uma solicitação `POST` para criar uma nova solicitação de exemplo. Esta será usada para verificar se os dados são preservados após o teste.
   - Exemplo de endpoint para criação de solicitação:
   
     ```http
     http://localhost:30010/solicitacoes/
     ```

   - Corpo da solicitação:

     ```json
     {
         "setor": "Financeiro",
         "solicitante": "Maria Silva",
         "produto": "Cadeira de escritório",
         "quantidade": 5,
         "status": "pendente"
     }
     ```

2. **Confirme que a Solicitação Foi Criada**:
   - Verifique se a solicitação foi armazenada com sucesso usando uma solicitação `GET` no endpoint `/solicitacoes/` para listar todas as solicitações.
   - Certifique-se de que a nova solicitação está presente na resposta.

3. **Desinstale a Release do Helm**:
   - Remova a aplicação usando o comando `helm uninstall`. Isso vai deletar os pods e outros recursos da aplicação, mas o volume persistente (PVC) será mantido.

     ```bash
     helm uninstall <nome-do-release>
     ```

   - Após a desinstalação, o PVC deve permanecer disponível, conforme indicado pela mensagem de confirmação de remoção.

4. **Reinstale a Release do Helm**:
   - Reinstale a aplicação, garantindo que o mesmo PVC seja reutilizado pela aplicação.

     ```bash
     helm install <nome-do-release> .
     ```

5. **Verifique a Persistência dos Dados**:
   - Após a reinstalação, verifique novamente a solicitação criada no primeiro passo usando uma solicitação `GET` no endpoint `/solicitacoes/`.
   - Se a solicitação ainda estiver presente, a persistência foi validada com sucesso, pois o PVC preservou os dados durante a desinstalação.

---

Explicação do Que Ocorre Durante o Processo

Esse teste demonstra o funcionamento da **persistência de dados com volumes persistentes (PVC e PV)** no Kubernetes:

1. **PVC e PV mantêm os dados**: 
   - Mesmo que a aplicação e seus pods sejam removidos, o **PersistentVolumeClaim (PVC)** e o **PersistentVolume (PV)** não são automaticamente excluídos. Isso ocorre porque o PV geralmente possui uma política de retenção (`Retain`), que preserva os dados no armazenamento subjacente.

2. **Reutilização do Volume Persistente na Reinstalação**:
   - Quando a aplicação é reinstalada, o PVC existente é reutilizado, o que permite à aplicação acessar os dados previamente armazenados no volume persistente. Dessa forma, as informações permanecem intactas e disponíveis.

3. **Conclusão**:
   - Esse comportamento permite a **persistência de dados** mesmo após a remoção de pods ou da aplicação, tornando os volumes persistentes ideais para armazenar dados críticos que precisam sobreviver a atualizações e reinicializações da aplicação.

Esse teste é fundamental para garantir que a aplicação lida adequadamente com a persistência de dados em um ambiente Kubernetes.

---

#### 6.8. Teste de Escalabilidade de Pods por Aumento de Consumo de CPU e Memória

Este guia descreve como realizar um teste de escalabilidade de pods em uma aplicação Kubernetes, com o objetivo de verificar a resposta do Kubernetes ao aumento de consumo de CPU e memória, escalando o número de réplicas conforme necessário para atender à carga.

---

1. **Verifique as Configurações do Horizontal Pod Autoscaler (HPA)**:
   - Antes de iniciar, verifique se o HPA está configurado para monitorar e escalar as réplicas da aplicação com base no uso de CPU e memória.
   - Confirme a configuração correta do HPA:

      ```bash
      kubectl get hpa
      kubectl describe hpa <nome-do-hpa>
      ```

---

2. **Inicie o Teste de Escalabilidade por Consumo de CPU**:

   - **Objetivo**: Testar a escalabilidade do Kubernetes aumentando o consumo de CPU para desencadear o escalonamento automático.
   
   - **Procedimento**:
     1. Use o menu interativo da aplicação ou envie uma solicitação `POST` para iniciar um teste de carga constante de CPU.

     - **Exemplo de código para iniciar o teste de CPU usando o menu interativo**:
       
       ```python
       simulate_cpu_scalability_test(max_orders=5000, delay=0.01)
       ```
   
     2. Aumente a carga gradualmente e observe o comportamento do HPA.
     
     3. Monitore o uso de CPU e o número de réplicas em tempo real:

       ```bash
       kubectl top pods -n <namespace> -w
       kubectl get hpa -w
       ```

   - **Métrica**: Observar se o HPA aumenta o número de pods conforme o uso de CPU atinge os limites configurados, garantindo a escalabilidade da aplicação.

---

3. **Inicie o Teste de Escalabilidade por Consumo de Memória**:

   - **Objetivo**: Testar a escalabilidade do Kubernetes aumentando o consumo de memória para desencadear o escalonamento automático.
   
   - **Procedimento**:
     1. Use o menu interativo da aplicação ou envie uma solicitação `POST` para iniciar o teste de carga constante de memória.

     - **Exemplo de código para iniciar o teste de memória usando o menu interativo**:
       
       ```python
       simulate_memory_scalability_test(duration=120, chunk_size=10**6)
       ```
   
     2. Aumente o consumo de memória gradualmente e observe o comportamento do HPA.
     
     3. Monitore o uso de memória e o número de réplicas em tempo real:

       ```bash
       kubectl top pods -n <namespace> -w
       kubectl get hpa -w
       ```

   - **Métrica**: Observar se o HPA aumenta o número de pods conforme o uso de memória atinge os limites configurados, proporcionando escalabilidade.

---

##### Explicação do Que Ocorre Durante o Processo

Este teste de escalabilidade ilustra o comportamento do HPA ao monitorar os recursos de CPU e memória da aplicação:

1. **Escalonamento Baseado em Limites de CPU e Memória**:
   - O HPA monitora continuamente o uso de CPU e memória. Quando o consumo atinge o valor-alvo configurado, o HPA aumenta o número de réplicas para balancear a carga.

2. **Resposta Dinâmica à Carga**:
   - O Kubernetes adiciona novos pods automaticamente até que o consumo de CPU ou memória fique dentro dos limites definidos, o que assegura a estabilidade da aplicação.

3. **Conclusão**:
   - Esse teste demonstra a **escalabilidade horizontal automática** do Kubernetes em resposta a aumentos de carga, garantindo resiliência e disponibilidade.

Este teste é essencial para verificar que a aplicação Kubernetes pode escalar em resposta ao aumento de demanda, mantendo o desempenho e a estabilidade da aplicação.

---

#### 6.9. **Teste de Recuperação de Falhas**

Este guia detalha como testar a recuperação de falhas em um cluster Kubernetes. O objetivo é verificar a resiliência do Kubernetes diante de falhas de pods e nós, observando como o cluster reage e se recupera automaticamente.

---

1. **Simulação de Falha de Pod**

   - **Objetivo**: Verificar a capacidade do Kubernetes de recriar automaticamente um pod em caso de falha.

   - **Procedimento**:
     1. Identifique um pod específico para simular a falha:

        ```bash
        kubectl get pods -n <namespace>
        ```

     2. Delete o pod manualmente para simular a falha:

        ```bash
        kubectl delete pod <nome-do-pod> -n <namespace>
        ```

     3. Após o comando de exclusão, observe como o Kubernetes recria automaticamente o pod para manter a disponibilidade.

     4. Monitore a recriação do pod em tempo real:

        ```bash
        kubectl get pods -n <namespace> -w
        ```

   - **Métrica**: Observe o tempo de recuperação do pod, que é o tempo que leva para que o Kubernetes recrie o pod e ele retorne ao status "Running". Esse tempo reflete a resiliência do cluster para lidar com falhas de pods.

---

2. **Simulação de Falha de Nó**

   - **Objetivo**: Avaliar a capacidade do Kubernetes de redistribuir a carga e reagendar pods quando um nó do cluster falha.

   - **Procedimento**:
     1. Identifique o nó onde os pods estão executando:

        ```bash
        kubectl get nodes
        kubectl get pods -o wide -n <namespace>
        ```

     2. Simule uma falha do nó:
        - Se estiver em um ambiente local (como Minikube ou Kind), você pode parar o nó virtual, interromper a máquina ou remover o nó do cluster.
        - Em um ambiente de nuvem, desligue a VM associada ao nó ou desconecte-a temporariamente.

     3. Após a simulação de falha, monitore o status dos nós para verificar a detecção da falha:

        ```bash
        kubectl get nodes -w
        ```

     4. Observe o comportamento do Kubernetes para redistribuir os pods para outros nós ativos no cluster.

   - **Métrica**: Observe o tempo de recuperação, incluindo o tempo que o Kubernetes leva para:
     - Detectar a falha do nó.
     - Reagendar os pods em outros nós disponíveis.

   Este tempo reflete a capacidade de recuperação do cluster e sua capacidade de manter a continuidade da aplicação mesmo diante de falhas de nós.

---

##### Explicação do Que Ocorre Durante o Processo

Este teste demonstra a **resiliência do Kubernetes** em cenários de falha de pods e nós:

1. **Recuperação de Pods**:
   - Quando um pod falha, o controlador de replicação do Kubernetes automaticamente cria um novo pod para substituir o que foi perdido, garantindo que o número desejado de réplicas esteja sempre disponível.

2. **Redistribuição de Carga em Caso de Falha de Nó**:
   - Em caso de falha de um nó, o Kubernetes detecta automaticamente o nó inativo e distribui os pods associados a ele para outros nós no cluster, mantendo a aplicação em operação.

3. **Conclusão**:
   - Esse teste é fundamental para validar a **capacidade de recuperação e a alta disponibilidade** do Kubernetes, mostrando como o cluster mantém a estabilidade e a disponibilidade da aplicação mesmo em cenários de falha.

Este teste fornece uma visão essencial da resiliência do Kubernetes, demonstrando sua capacidade de recuperação em cenários de falha de pods e nós, o que é essencial para garantir a continuidade das operações em ambientes de produção.

---

#### 6.10. **Teste de Upgrade de Template Helm**

Este guia detalha como testar a resiliência da aplicação Kubernetes durante uma atualização de template Helm. O objetivo é avaliar o impacto de uma atualização no comportamento da aplicação, observando se o Helm consegue aplicar mudanças sem interromper o serviço.

---

1. **Preparação para o Upgrade do Template Helm**

   - **Objetivo**: Verificar o estado inicial do cluster e da aplicação antes de aplicar qualquer atualização.

   - **Procedimento**:
     1. **Verifique o estado atual dos recursos Helm**:
   
        ```bash
        helm list
        ```
   
     2. **Inspecione os pods, serviços e demais recursos da aplicação** para confirmar que estão em estado saudável:

        ```bash
        kubectl get pods -n <namespace>
        kubectl get services -n <namespace>
        ```

---

2. **Atualize o Template Helm**

   - **Objetivo**: Aplicar uma atualização nos templates Helm da aplicação e observar o efeito na execução dos serviços.

   - **Procedimento**:
     1. Abra o template Helm que deseja atualizar, por exemplo, um arquivo em `templates/deployment.yaml` ou `values.yaml`.
   
     2. Modifique o template conforme necessário, podendo incluir:
        - Alterações na configuração de CPU ou memória (`resources.requests` e `resources.limits`).
        - Ajustes na definição de réplicas (`replicaCount`).
        - Modificações de variáveis de ambiente ou configurações específicas do container.
   
     3. **Salve as alterações** e aplique a atualização usando o comando `helm upgrade`:
   
```bash
helm upgrade <nome-do-release> <caminho-do-chart> -f <values-file>
```

---

3. **Monitore o Comportamento da Aplicação Durante o Upgrade**

   - **Objetivo**: Avaliar a continuidade do serviço durante a atualização e identificar qualquer interrupção temporária.

   - **Procedimento**:
     1. Observe o status dos pods em tempo real para identificar reinicializações ou interrupções:

        ```bash
        kubectl get pods -n <namespace> -w
        ```
   
     2. Monitore também os logs dos pods durante o upgrade para capturar qualquer mensagem de erro ou comportamento inesperado:

        ```bash
        kubectl logs <nome-do-pod> -n <namespace> -f
        ```

     3. Verifique o status dos serviços e endpoints para garantir que a aplicação continua respondendo a solicitações:

        ```bash
        kubectl get services -n <namespace>
        kubectl get endpoints -n <namespace>
        ```

   - **Métrica**: Avalie se o Helm conseguiu aplicar o upgrade sem causar downtime significativo ou falhas. O ideal é que a atualização ocorra com uma transição suave e sem interrupções perceptíveis para os usuários.

---

##### Explicação do Que Ocorre Durante o Processo

Este teste ilustra como o Helm aplica atualizações no cluster e os efeitos dessa atualização na continuidade da aplicação:

1. **Upgrade Incremental de Recursos**:
   - O Helm tenta aplicar as mudanças de forma incremental, o que significa que novos pods podem ser criados com as configurações atualizadas enquanto os pods antigos ainda estão ativos, garantindo uma transição gradual e contínua.

2. **Impacto de Alterações em Recursos e Configurações**:
   - Alterações significativas em recursos (como limites de CPU e memória) podem causar reinicializações de pods, mas o Kubernetes tenta manter o número desejado de réplicas em execução para minimizar o impacto.

3. **Conclusão**:
   - Esse teste demonstra a **capacidade do Helm de gerenciar upgrades de maneira controlada**, aplicando atualizações enquanto minimiza o impacto nos serviços, o que é fundamental para garantir uma experiência contínua para o usuário.

Esse teste é essencial para validar o processo de atualização de templates Helm em um cluster Kubernetes, garantindo que a aplicação suporta modificações de configuração sem causar interrupções significativas.


Sim, essa abordagem mais simples pode ser realizada. Alterando o tamanho do `PersistentVolume` para 100Mi e o `PersistentVolumeClaim` para 10Mi, você pode realizar um teste prático em que solicita um número de PVCs até que o armazenamento do PV seja esgotado. Aqui está um guia para configurar e executar o teste:

---

### 6.11. **Teste Simplificado de Capacidade de Armazenamento (Storage)**

1. **Configuração Inicial do PersistentVolume (PV)**

   - **Objetivo**: Criar um PV com capacidade limitada de armazenamento, a fim de atingir rapidamente o limite de alocação com múltiplos PVCs.

   - **Procedimento**:
     1. Defina o PV em um arquivo `storage-capacity-pv-100.yaml` com um tamanho reduzido, como 100Mi. Exemplo:

        ```yaml
        apiVersion: v1
        kind: PersistentVolume
        metadata:
          name: storage-test-pv
        spec:
          capacity:
            storage: 100Mi
          accessModes:
            - ReadWriteOnce
          persistentVolumeReclaimPolicy: Retain
          storageClassName: manual-storage
          hostPath:
            path: "/mnt/data"
        ```

     2. Aplique o PV no cluster:

        ```bash
        kubectl apply -f storage-capacity-pv-100.yaml
        ```

---

#### 2. **Configuração do PersistentVolumeClaim (PVC)**

   - **Objetivo**: Criar PVCs menores (10Mi cada) que solicitam espaço do PV até que a capacidade do PV seja completamente alocada.

   - **Procedimento**:
     1. Defina o PVC em um arquivo `storage-capacity-pvc-10.yaml` com um tamanho de 10Mi, associado ao `StorageClass` do PV. Exemplo:

        ```yaml
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          generateName: storage-test-pvc-
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 10Mi
          storageClassName: manual-storage
        ```

     2. Utilize um loop para criar PVCs até que o PV de 100Mi seja totalmente consumido. Execute o comando abaixo:

        ```bash
        for i in {1..10}; do
          kubectl apply -f storage-capacity-pvc-10.yaml
          sleep 5  # Pausa breve entre as criações para observar a alocação
        done
        ```

---

Esse comando com `for i in {1..10}; do ... done` é específico para **Linux** e **Mac** (ou sistemas compatíveis com bash). Ele **não funciona diretamente no prompt de comando do Windows**, mas funciona em um terminal **WSL** (Windows Subsystem for Linux), **PowerShell** com adaptação, ou em terminais como **Git Bash**.

### Alternativa para Windows (PowerShell)
Em PowerShell, você pode adaptar o loop para rodar comandos repetidamente. Aqui está como fazer isso:

```powershell
for ($i = 1; $i -le 10; $i++) {
  kubectl apply -f storage-capacity-pvc-10.yaml
  Start-Sleep -Seconds 1  # Pausa breve entre as criações para observar a alocação
}
```

Essas adaptações garantem que o script de criação dos PVCs rode tanto em ambientes Linux quanto Windows com PowerShell ou WSL.

---

#### 3. **Monitoramento da Capacidade e Limite do Armazenamento**

   - **Objetivo**: Observar como o Kubernetes reage ao esgotamento da capacidade do PV.

   - **Procedimento**:
     1. Use `kubectl get pvc` para monitorar o status de cada PVC e ver quais foram alocados com sucesso:

        ```bash
        kubectl get pvc -w
        ```

     2. Verifique o PV para observar seu status de alocação e ver quando ele atinge o limite:

        ```bash
        kubectl get pv
        ```

     3. Verifique se algum PVC fica em estado “Pending” devido à falta de espaço disponível e observe eventos ou logs para mensagens de erro:

        ```bash
        kubectl get events --sort-by=.metadata.creationTimestamp
        ```

---

#### Explicação do Que Ocorre Durante o Processo

Ao configurar o PV para um tamanho total de 100Mi e solicitar PVCs de 10Mi cada, o Kubernetes continuará alocando o armazenamento até que o PV esteja esgotado. Aqui está o que ocorre:

1. **Alocação e Esgotamento do PV**:
   - Cada PVC consome 10Mi do PV até que a capacidade de 100Mi seja atingida, após o qual novas solicitações de PVC resultam em um status “Pending”, indicando falta de capacidade.

2. **Capacidade de Resposta do Kubernetes**:
   - O Kubernetes reflete o estado de alocação com precisão, gerando mensagens de erro ou avisos nos logs quando o limite de armazenamento é atingido, e evita alocações acima da capacidade do PV.

3. **Conclusão**:
   - Este teste permite verificar a resposta do Kubernetes quando a capacidade do armazenamento é esgotada, ajudando a entender a capacidade de armazenamento e a resposta a solicitações adicionais.

Essa abordagem simplificada permite um teste rápido e direto da capacidade de armazenamento no cluster, sendo uma forma eficaz de observar o comportamento do Kubernetes ao atingir o limite do armazenamento alocado.

### Outros Testes Não Implementados

#### 1 **Teste de Balanceamento de Carga**

   - **Objetivo**: Garantir que o Kubernetes distribui as requisições de maneira uniforme entre os pods.
   - **Procedimento**:
     - Crie um serviço com múltiplos pods e exponha-o usando um `LoadBalancer` ou `NodePort`.
     - Envie requisições consecutivas ao serviço (usando ferramentas como `ab`, `wrk` ou `hey`) e verifique se elas são distribuídas entre os pods de maneira equilibrada.
   - **Métrica**: Distribuição das requisições entre os pods; tempo de resposta médio.

### 2. **Teste de Segurança de Rede e Isolamento**

   - **Objetivo**: Avaliar a segurança do Kubernetes em termos de isolamento entre pods e namespaces.
   - **Procedimento**:
     - Configure `NetworkPolicies` para restringir o tráfego entre pods e namespaces.
     - Tente acessar pods de um namespace a partir de outro para verificar se as políticas de rede estão sendo aplicadas corretamente.
   - **Métrica**: Capacidade de isolar e proteger o tráfego entre diferentes pods e namespaces.

### 3. **Teste de Latência de Rede entre Pods**

   - **Objetivo**: Avaliar o tempo de comunicação entre os pods, especialmente para aplicações distribuídas.
   - **Procedimento**:
     - Use ferramentas como `ping` ou `iperf` para medir a latência entre diferentes pods.
     - Avalie o impacto da latência no desempenho geral da aplicação.
   - **Métrica**: Tempo médio de latência entre os pods.

### 4. **Teste de Monitoramento e Alertas**

   - **Objetivo**: Verificar se o Kubernetes e as ferramentas de monitoramento integradas detectam e reportam eventos críticos.
   - **Procedimento**:
     - Configurar monitoramento com ferramentas como Prometheus e Grafana.
     - Simular cenários de carga e falhas e observar se as métricas e alertas são acionados corretamente.
   - **Métrica**: Precisão e velocidade de resposta dos alertas e gráficos de monitoramento.