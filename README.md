# Sistema Ponto

Este repositório contém o código-fonte para um sistema de controle de ponto de funcionários, desenvolvido como uma demonstração e não como um projeto real. O objetivo deste projeto é apresentar conceitos de desenvolvimento em Python, manipulação de dados, e armazenamento de informações relacionadas ao controle de ponto. 

## Estrutura do Repositório

A seguir, uma visão geral da estrutura de arquivos e suas funcionalidades:

### Arquivos do Projeto

- `main.py`
    - **Descrição**: Este é o arquivo principal que inicia a execução do sistema. Ele contém a lógica de fluxo principal, onde as interações do usuário são gerenciadas.
    - **Funcionalidade**: Carrega as configurações iniciais, exibe o menu para o usuário e chama as funções apropriadas com base nas entradas do usuário.

- `funcionario.py`
    - **Descrição**: Este arquivo contém a definição da classe `Funcionario`, que representa um funcionário no sistema.
    - **Funcionalidade**: A classe possui atributos como `nome`, `cpf`, `horario_entrada`, `horario_saida` e métodos para registrar o ponto, calcular horas trabalhadas e exibir informações do funcionário.

- `sistema_ponto.py`
    - **Descrição**: Este arquivo contém a definição da classe `SistemaPonto`, responsável por gerenciar os registros de ponto dos funcionários.
    - **Funcionalidade**: Possui métodos para adicionar funcionários, registrar horários de entrada e saída, e gerar relatórios de ponto.

- `relatorio.py`
    - **Descrição**: Este arquivo é responsável pela geração de relatórios com base nos dados de ponto dos funcionários.
    - **Funcionalidade**: Contém funções para formatar e apresentar dados de forma amigável, permitindo que os administradores visualizem as informações de forma clara.

- `database.py`
    - **Descrição**: Este arquivo simula uma interface de banco de dados para armazenar informações dos funcionários e registros de ponto.
    - **Funcionalidade**: Implementa funções para adicionar, recuperar e excluir dados, além de simular a persistência dos dados entre as execuções do programa.

- `README.md`
    - **Descrição**: Este arquivo é a documentação do projeto, que fornece uma visão geral, instruções de uso e informações sobre a estrutura do código.
    - **Funcionalidade**: Ajuda os desenvolvedores e mantenedores a entenderem rapidamente a estrutura e a lógica do projeto.

### Instalação

Para executar o sistema, você precisará ter o Python instalado em sua máquina. Siga os passos abaixo para instalar e executar o projeto:

1. Clone o repositório:
    ```bash
    git clone https://github.com/S4MU3LDemolidor/Sistema-Ponto.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Sistema-Ponto
    ```

3. Execute o arquivo principal:
    ```bash
    python main.py
    ```

### Uso

O sistema apresentará um menu interativo que permitirá ao usuário:
- Adicionar novos funcionários.
- Registrar horários de entrada e saída.
- Visualizar relatórios de ponto.

### Contribuições

Contribuições são bem-vindas! Se você deseja melhorar este projeto ou adicionar novos recursos, sinta-se à vontade para abrir um *pull request*.

### Licença

Este projeto é fornecido sem garantias de qualquer tipo. Utilize-o por sua conta e risco. Este sistema é uma demonstração e não deve ser usado em produção.

---

Sinta-se à vontade para modificar e adaptar este documento conforme necessário.