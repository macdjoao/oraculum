import random

from faker import Faker

from src.infra.repositories.grade import Grade as GradeRepository
from src.infra.repositories.player import Player as PlayerRepository
from src.infra.repositories.race import Race as RaceRepository

fake = Faker()
player = PlayerRepository()
race = RaceRepository()
grade = GradeRepository()


def test_insert_player():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    player_name = (fake.first_name()).capitalize()
    player.insert(name=player_name, race=race_name, grade=grade_name)

    response = str(player.select_one(name=player_name))

    assert (
        response
        == f'Player (name = {player_name}, level = 1, race = {race_name}, grade = {grade_name})'
    )

    # Cleaning DB
    player.delete(name=player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)


def test_update_level():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    player_name = (fake.first_name()).capitalize()
    player.insert(name=player_name, race=race_name, grade=grade_name)

    new_level = random.randint(2, 15)
    player.update_level(name=player_name, level=new_level)

    response = str(player.select_one(name=player_name))

    assert (
        response
        == f'Player (name = {player_name}, level = {new_level}, race = {race_name}, grade = {grade_name})'
    )

    # Cleaning DB
    player.delete(name=player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)
