# Oraculum
Um projeto simples para estudos e aplicação de SQLAlchemy e PyTest, seguindo os padrões de Clean Code e Clean Architecture.

## Resumo
Oraculum é uma aplicação que tem o objetivo de armazenar fichas de personagens de RPG.

## Instalação
1. Clone o projeto em seu computador:
```sh
you@pc:~$ git clone https://github.com/macdjoao/oraculum.git
```
2. Instale as dependências utilizando Poetry (se preferir, crie antes seu ambiente virtual com *you@pc:~/oraculum$ poetry shell*):
```sh
you@pc:~/oraculum$ poetry install
```
## Configuração
1. Crie um arquivo **.env** do diretório **src/**, e preencha as constantes de acordo com o arquivo **.env.sample**
2. Crie e execute o container Docker:
```sh
you@pc:~/oraculum$ docker-compose up -d
```
3. Aplique as migrações utilizando Alembic:
```sh
you@pc:~/oraculum$ alembic upgrade head
```
## Uso
Para utilizar as funcionalidades, crie um arquivo **.py** e importe as classes que estão nos arquivos **.py** em **src/infra/repositories/**. Salve instâncias das classes em variáveis, e use as funções como preferir.

## Testes Unitários
Para executar os testes:
```sh
you@pc:~/oraculum$ pytest -v
```
Nota:
> Para os testes "test_grade_select_all_no_record_error", "test_race_select_all_no_record_error" e "test_player_select_all_no_record_error" passarem, a base de dados deve estar sem registros.

## Informações sobre o desenvolvimento
- [SQLAlchemy](https://www.sqlalchemy.org/) e [Alembic](https://alembic.sqlalchemy.org/en/latest/): ORM e Migrações
- [PyTest](https://docs.pytest.org/en/7.3.x/) e [Faker](https://faker.readthedocs.io/en/master/): Testes Unitários e geração de dados fake
- [Docker](https://www.docker.com/) e [imagem PostgreSQL](https://hub.docker.com/_/postgres): Banco de Dados
- [Poetry](https://python-poetry.org/): Gerenciamento de pacotes Python
- [Blue](https://blue.readthedocs.io/en/latest/) e [isort](https://pycqa.github.io/isort/): Formatação de código Python
- [pre-commit](https://pre-commit.com/): Automação da formatação de código ao realizar commit

## Contribuição
Pull requests são bem vindas. Caso tenha interesse em contribuir com o projeto, você pode ler as sugestões iniciais no trecho To Do desse arquivo, ou mesmo analisar o código e sugerir novas features ou refatorações.

## To Do
- [ ] Separar "Base" e as entidades (em models.py) em arquivos próprios (por ora não foi possível, pois "target_metadata = Base.metadata" (em alembic/env.py) não reconhece as entidades quando "Base" e as entidades estão em arquivos próprios).

## Licença

[MIT](https://choosealicense.com/licenses/mit/)