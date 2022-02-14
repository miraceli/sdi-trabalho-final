# Implementação de um Serviço utilizando Comunicação Inter-processos através de Remote Method Invocation - RMI

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

![Badge](https://img.shields.io/badge/Made_with-docker-%237159c1?style=for-the-badge&logo=docker&labelColor=blue&color=darkblue&logoColor=white)

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)


Aplicação feita para a apresentação de trabalho final da disciplina de Sistemas Distribuídos da turma 2021/2 do curso de TADS da UDESC. 
O objetivo é implementar um serviço de echo de mensagem remota com replicação das mensagens entre servidores, como forma de garantir tolerância a falhas.
A implementação foi realizada utilizando-se comunicação Inter-Processos por meio de RMI em linguagem Python3, com a biblioteca Pyro4.0.

### Features

- [x] Envio de mensagens
- [x] Lista de mensagens enviadas


### Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina as seguintes ferramentas:
- [Git](https://git-scm.com)
- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- SO Linux
 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/) e um ambiente Linux. Obs: O desenvolvimento e testes desta aplicação foram criados utilizando Windows com [WSL2](https://docs.microsoft.com/pt-br/windows/wsl/install).

### 🛠 Tecnologias

As seguintes ferramentas foram usadas no projeto:

- [VSCode](https://code.visualstudio.com/)
- [Windows Terminal](https://www.microsoft.com/pt-br/p/windows-terminal/9n0dx20hk701)

### 🎲 Rodando o projeto

```bash
# Clone este repositório
$ git clone <https://github.com/miraceli/SistemaLoginPython>

# Acesse a pasta do projeto no terminal/cmd
$ cd sdi-trabalho-final

# Dê permissão de execução para os programas Shell
$ chmod +x ./server.sh
$ chmod +x ./client.sh

# Execute o server 
$ sh. server.sh

# Execute o client
$ sh. client.sh
```


### 🔧 Contribuições
Fique a vontade para sugerir melhorias e/ou fazer contribuições.


### 🎯 Autores
[Miraceli Bonjardim](https://linkedin.com/in/miraceli)

[Luiz Costa](https://github.com/LuizCostaa)
