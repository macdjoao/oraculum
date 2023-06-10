import random

from faker import Faker

from src.infra.repositories.grade import Grade as GradeRepository
from src.infra.repositories.player import Player as PlayerRepository
from src.infra.repositories.race import Race as RaceRepository

fake = Faker()
player = PlayerRepository()
race = RaceRepository()
grade = GradeRepository()


def test_player_insert():

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


def test_player_delete():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    player_name = (fake.first_name()).capitalize()
    player.insert(name=player_name, race=race_name, grade=grade_name)

    response = str(player.delete(name=player_name))

    # Cleaning DB
    player.delete(name=player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)

    assert response == f'Player deleted: {player_name}'


def test_player_update_name():

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


def test_player_update_level():

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


def test_player_update_race():

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


def test_player_update_grade():

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


def test_player_select_all_no_record_error():

    response = str(player.select_all())

    assert response == 'Error: No Player record found'


def test_player_select_one_not_found_error():

    name = (fake.word()).capitalize()

    response = str(player.select_one(name=name))

    assert response == f'Error: Player {name} not found'


def test_player_insert_incomplete_param_error_name():

    race = fake.word()
    grade = fake.word()

    response = str(player.insert(race=race, grade=grade))

    assert response == f'Error: Missing param "name" in Player'


def test_player_insert_incomplete_param_error_race():

    name = (fake.word()).capitalize()
    grade = fake.word()

    response = str(player.insert(name=name, grade=grade))

    assert response == f'Error: Missing param "race" in Player'


def test_player_insert_incomplete_param_error_grade():

    name = (fake.word()).capitalize()
    race = (fake.word()).capitalize()

    response = str(player.insert(name=name, race=race))

    assert response == f'Error: Missing param "grade" in Player'


def test_player_insert_already_registered_error_name():

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    already_player_name = fake.first_name()
    player.insert(name=already_player_name, race=race_name, grade=grade_name)

    response = str(
        player.insert(
            name=already_player_name, race=race_name, grade=grade_name
        )
    )

    # Cleaning DB
    player.delete(name=already_player_name)
    race.delete(name=race_name)
    grade.delete(name=grade_name)

    assert (
        response == f'Error: Player {already_player_name} already registered'
    )


def test_player_insert_race_not_found_error():

    race_name = (fake.word()).capitalize()

    grade_name = (fake.word()).capitalize()
    grade.insert(name=grade_name)

    already_player_name = fake.first_name()
    player.insert(name=already_player_name, race=race_name, grade=grade_name)

    response = str(
        player.insert(
            name=already_player_name, race=race_name, grade=grade_name
        )
    )

    # Cleaning DB
    player.delete(name=already_player_name)
    grade.delete(name=grade_name)

    assert response == f'Error: Race {race_name} not found'


def test_player_insert_grade_not_found_error():

    grade_name = (fake.word()).capitalize()

    race_name = (fake.word()).capitalize()
    race.insert(name=race_name)

    already_player_name = fake.first_name()
    player.insert(name=already_player_name, race=race_name, grade=grade_name)

    response = str(
        player.insert(
            name=already_player_name, race=race_name, grade=grade_name
        )
    )

    # Cleaning DB
    player.delete(name=already_player_name)
    race.delete(name=race_name)

    assert response == f'Error: Grade {grade_name} not found'


def test_player_delete_incomplete_param_error_name():

    response = str(player.delete())

    assert response == f'Error: Missing param "name" in Player'


def test_player_delete_not_found_error_name():

    name = fake.first_name()

    response = str(player.delete(name=name))

    assert response == f'Error: Player {name} not found'


def test_player_update_name_incomplete_param_error_actual_name():

    response = str(player.update_name())

    assert response == f'Error: Missing param "actual_name" in Player'


def test_player_update_name_incomplete_param_error_new_name():

    actual_name = fake.first_name()

    response = str(player.update_name(actual_name=actual_name))

    assert response == f'Error: Missing param "new_name" in Player'


def test_player_update_name_not_found_error_actual_name():

    actual_name = fake.first_name()
    new_name = fake.first_name()

    response = str(
        player.update_name(actual_name=actual_name, new_name=new_name)
    )

    assert response == f'Error: Player {actual_name} not found'


def test_player_update_name_already_registered_error_new_name():

    race_sample = fake.word()
    race.insert(name=race_sample)

    grade_sample = fake.word()
    grade.insert(name=grade_sample)

    first_player_sample = fake.first_name()
    player.insert(
        name=first_player_sample, race=race_sample, grade=grade_sample
    )

    second_player_sample = fake.first_name()
    player.insert(
        name=second_player_sample, race=race_sample, grade=grade_sample
    )

    response = str(
        player.update_name(
            actual_name=first_player_sample, new_name=second_player_sample
        )
    )

    # Cleaning DB
    player.delete(name=first_player_sample)
    player.delete(name=second_player_sample)
    race.delete(name=race_sample)
    grade.delete(name=grade_sample)

    assert (
        response == f'Error: Player {second_player_sample} already registered'
    )


def test_player_update_level_incomplete_param_error_name():

    new_level = random.randint(2, 15)

    response = str(player.update_level(level=new_level))

    assert response == f'Error: Missing param "name" in Player'


def test_player_update_level_incomplete_param_error_level():

    name = fake.first_name()

    response = str(player.update_level(name=name))

    assert response == f'Error: Missing param "level" in Player'


def test_player_update_level_not_int():

    name = fake.first_name()
    new_level = fake.word()

    response = str(player.update_level(name=name, level=new_level))

    assert response == f'Error: Param "level" is not a integer'


def test_player_update_level_player_not_found():

    name = fake.last_name()
    new_level = random.randint(2, 15)

    response = str(player.update_level(name=name, level=new_level))

    assert response == f'Error: Player {name} not found'


def test_player_update_race_incomplete_param_error_name():

    race = fake.word()

    response = str(player.update_race(race=race))

    assert response == f'Error: Missing param "name" in Player'
