from faker import Faker

from src.infra.repositories.race import Race as RaceRepository

fake = Faker()
race = RaceRepository()


def test_insert_race():

    name = (fake.word()).capitalize()

    race.insert(name=name)
    response = str(race.select_one(name=name))

    # Cleaning DB
    race.delete(name=name)

    assert response == f'Race (name = {name})'


def test_update_race_name():

    actual_name = (fake.word()).capitalize()
    new_name = (fake.word()).capitalize()

    race.insert(name=actual_name)

    update_response = str(
        race.update_name(actual_name=actual_name, new_name=new_name)
    )
    select_response = str(race.select_one(name=new_name))

    # Cleaning DB
    race.delete(name=new_name)

    assert update_response == f'Race updated: {new_name}'
    assert select_response == f'Race (name = {new_name})'


def test_delete_race():

    name = (fake.word()).capitalize()

    race.insert(name=name)
    response = str(race.delete(name=name))

    assert response == f'Race deleted: {name}'


def test_race_select_all_no_record_error():

    response = str(race.select_all())

    assert response == 'Error: No Race record found'


def test_race_select_one_not_found_error():

    name = (fake.word()).capitalize()

    response = str(race.select_one(name=name))

    assert response == f'Error: Race {name} not found'


def test_race_select_one_incomplete_param_error_name():

    response = str(race.select_one())

    assert response == f'Error: Missing param "name" in Race'
