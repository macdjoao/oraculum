# Oraculum
Um projeto simples para estudos e aplicação de SQLAlchemy e PyTest, seguindo os padrões de Clean Code.

## Resumo
Oraculum é uma aplicação que tem o objetivo de armazenar fichas de personagens de RPG.

## Instalação
1. Clone o projeto em seu computador:
```sh
$ git clone https://github.com/macdjoao/oraculum.git
```

2. Instale as dependências utilizando Poetry (se preferir, crie antes seu ambiente virtual com *you@pc:~/oraculum$ poetry shell*):
```sh
~/oraculum$ poetry install
```

## Configuração
1. Crie um arquivo **.env** do diretório **src/**, e preencha as constantes de acordo com o arquivo **.env.sample**

2. Crie e execute o container Docker:
```sh
~/oraculum$ docker-compose up -d
```

3. Aplique as migrações utilizando Alembic:
```sh
~/oraculum$ alembic upgrade head
```
## Uso
Para utilizar as funcionalidades, crie um arquivo **.py** e importe as classes que estão nos arquivos **.py** em **src/infra/repositories/**. Salve instâncias das classes em variáveis, e use as funções como preferir:

```python
from src.infra.repositories.race import Race as RaceRepository

your_race = RaceRepository()

your_race.insert(name='Elf')
your_race.select_all()
your_race.select_one(name='Elf')
your_race.update_name(actual_name='Elf', new_name='Orc')
your_race.delete(name='Orc')
```

```python
from src.infra.repositories.grade import Grade as GradeRepository

your_grade = RaceRepository()

your_grade.insert(name='Archer')
your_grade.select_all()
your_grade.select_one(name='Archer')
your_grade.update_name(actual_name='Archer', new_name='Mage')
your_grade.delete(name='Mage')
```

```python
from src.infra.repositories.player import Player as PlayerRepository

your_player = PlayerRepository()

your_player.insert(name='John', race='Elf', grade='Archer')
your_player.select_all()
your_player.select_one(name='John')
your_player.update_name(actual_name='John', new_name='Doe')
your_player.update_grade(name='Doe', grade='Warrior')
your_player.update_race(name='Doe', race='Dwarf')
your_player.update_level(name='Doe', level=2)
your_player.delete(name='Doe')
```

## Testes Unitários
Para executar os testes:

```sh
~/oraculum$ pytest -v
```

Nota:

> Para os testes "test_grade_select_all_no_record_error", "test_race_select_all_no_record_error" e "test_player_select_all_no_record_error" passarem, a base de dados deve estar sem registros.

![Tests PrintScreen](tests-printscr.png)

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
