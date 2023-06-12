# Oraculum
Um projeto simples para estudos e aplicação de SQLAlchemy e PyTest, seguindo os padrões de Clean Code e Clean Architecture.

## Resumo
Oraculum é uma aplicação que tem o objetivo de armazenar fichas de personagens de RPG.

## Instalação

## Para usuários

## Para desenvolvedores

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
[ ] Separar "Base" e as entidades (em models.py) em arquivos próprios (por ora não foi possível, pois "target_metadata = Base.metadata" (em alembic/env.py) não reconhece as entidades quando "Base" e as entidades estão em arquivos próprios).

## Licença

[MIT](https://choosealicense.com/licenses/mit/)