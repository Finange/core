# Core of Finange's Backend!


## Como usar:

#### 1 - Instalar o `poetry` na sua maquina para poder instalar as bibliotecas do projeto e usar a sua maquina virtual. Use esse link para instalar na sua maquina: `https://python-poetry.org/docs/`
#### 2 - Faça o clone do projeto
#### 3 - Entre na pasta do projeto
#### 4 - Rode o comando `poetry shell` para o poetry criar uma maquina virtual dentro do projeto e conseguir instalar as dependencias
#### 5 - Rode o comando `poetry install` para o poetry instalar as bibliotecas do projeto
#### 6 - Rode o comando `pre-commit install` para o pre-commit instalar os hooks de verificação do projeto
#### 7 - Crie um bot no telegram para o projeto, veja [aqui](https://core.telegram.org/bots#3-how-do-i-create-a-bot) como criar um bot para o telegram.
#### 8 - Crie o arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```
DEBUG=True
BOT_TOKEN="{SEU_TOKEN DO TELEGRAM}"
```

#### 9 - Rode o comando `python3 manage.py migrate` para o poetry criar as tabelas do banco de dados
#### 10 - Rode o comando `python3 manage.py runserver` para rodar o projeto.
