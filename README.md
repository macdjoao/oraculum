# Oraculum
Um projeto simples para estudos e aplicação de SQLAlchemy e PyTest, seguindo os padrões de Clean Code e Clean Architecture.

## Resumo
Oraculum é uma aplicação que tem como objetivo armazenar fichas de personagens de RPG.

## Instalação

## Para usuários

## Para desenvolvedores

## Informações sobre o desenvolvimento
ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
Migrações de Banco de Dados: [Alembic](https://alembic.sqlalchemy.org/en/latest/)
Testes: [PyTest](https://docs.pytest.org/en/7.3.x/)

Plataforma de desenvolvimento: [WSL2](https://learn.microsoft.com/pt-br/windows/wsl/install) ([Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy/))
Editor de Texto: [Visual Studio Code](https://code.visualstudio.com/)
Container: [Docker](https://www.docker.com/)
Banco de Dados: [PostgreSQL](https://www.postgresql.org/)
Ferramenta para administração da base de dados: [DBeaver](https://dbeaver.io/download/)
Gerenciador de Pacotes Python: [Poetry](https://python-poetry.org/)
Formatadores de Código Python: [Blue](https://blue.readthedocs.io/en/latest/) e [isort](https://pycqa.github.io/isort/)
Automação de formatação: [pre-commit](https://pre-commit.com/)

## Contribuição
Pull requests são bem vindas. Caso tenha interesse em contribuir com o projeto, você pode ler as sugestões iniciais no trecho To Do desse arquivo, ou mesmo analisar o código e sugerir novas features ou refatorações.

## To Do
- Separar "Base" e as entidades (em models.py) em arquivos próprios. Por ora não foi possível, pois "target_metadata = Base.metadata" (em alembic/env.py) não reconhece as entidades quando "Base" e as entidades estão em arquivos próprios.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)