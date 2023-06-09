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

    # Cleaning DB
    player.delete(name=player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)

    assert (
        response
        == f'Player (name = {player_name}, level = 1, race = {race_name}, grade = {grade_name})'
    )


def test_update_player_name():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    actual_player_name = (fake.first_name()).capitalize()
    player.insert(name=actual_player_name, race=race_name, grade=grade_name)

    new_player_name = (fake.first_name()).capitalize()
    update_response = str(
        player.update_name(
            actual_name=actual_player_name, new_name=new_player_name
        )
    )
    select_response = str(player.select_one(name=new_player_name))

    # Cleaning DB
    player.delete(name=new_player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)

    assert update_response == f'Player updated: {new_player_name}'
    assert (
        select_response
        == f'Player (name = {new_player_name}, level = 1, race = {race_name}, grade = {grade_name})'
    )


def test_update_player_level():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    player_name = (fake.first_name()).capitalize()
    player.insert(name=player_name, race=race_name, grade=grade_name)

    new_level = random.randint(2, 15)
    player.update_level(name=player_name, level=new_level)

    response = str(player.select_one(name=player_name))

    # Cleaning DB
    player.delete(name=player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)

    assert (
        response
        == f'Player (name = {player_name}, level = {new_level}, race = {race_name}, grade = {grade_name})'
    )


def test_update_player_race():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    player_name = (fake.first_name()).capitalize()
    player.insert(name=player_name, race=race_name, grade=grade_name)

    new_race = (fake.word()).capitalize()
    race.insert(name=new_race)
    player.update_race(name=player_name, race=new_race)

    response = str(player.select_one(name=player_name))

    # Cleaning DB
    player.delete(name=player_name)
    grade.delete(name=grade_name)
    race.delete(name=race_name)
    race.delete(name=new_race)

    assert (
        response
        == f'Player (name = {player_name}, level = 1, race = {new_race}, grade = {grade_name})'
    )


def test_update_player_grade():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    player_name = (fake.first_name()).capitalize()
    player.insert(name=player_name, race=race_name, grade=grade_name)

    new_grade = (fake.word()).capitalize()
    grade.insert(name=new_grade)
    player.update_grade(name=player_name, grade=new_grade)

    response = str(player.select_one(name=player_name))

    # Cleaning DB
    player.delete(name=player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)
    grade.delete(name=new_grade)

    assert (
        response
        == f'Player (name = {player_name}, level = 1, race = {race_name}, grade = {new_grade})'
    )