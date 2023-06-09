from faker import Faker

from src.infra.repositories.race import Race as RaceRepository

fake = Faker()
race = RaceRepository()


def test_race_insert():

    name = (fake.word()).capitalize()

    race.insert(name=name)
    response = str(race.select_one(name=name))

    # Cleaning DB
    race.delete(name=name)

    assert response == f'Race (name = {name})'


def test_race_update_name():

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


def test_race_delete():

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


def test_race_insert_incomplete_param_error_name():

    response = str(race.insert())

    assert response == f'Error: Missing param "name" in Race'


def test_race_insert_already_registered_error_name():

    already_race_name = fake.first_name()
    race.insert(name=already_race_name)

    response = str(race.insert(name=already_race_name))

    # Cleaning DB
    race.delete(name=already_race_name)

    assert response == f'Error: Race {already_race_name} already registered'


def test_race_delete_incomplete_param_error_name():

    response = str(race.delete())

    assert response == f'Error: Missing param "name" in Race'


def test_race_delete_not_found_error_name():

    name = fake.first_name()

    response = str(race.delete(name=name))

    assert response == f'Error: Race {name} not found'


def test_race_update_incomplete_param_error_actual_name():

    response = str(race.update_name())

    assert response == f'Error: Missing param "actual_name" in Race'


def test_race_update_incomplete_param_error_new_name():

    actual_name = fake.first_name()

    response = str(race.update_name(actual_name=actual_name))

    assert response == f'Error: Missing param "new_name" in Race'


def test_race_update_not_found_error_actual_name():

    actual_name = fake.first_name()
    new_name = fake.first_name()

    response = str(
        race.update_name(actual_name=actual_name, new_name=new_name)
    )

    assert response == f'Error: Race {actual_name} not found'


def test_race_update_already_registered_error_new_name():

    actual_race_sample = fake.first_name()
    race.insert(name=actual_race_sample)

    already_race_sample = fake.first_name()
    race.insert(name=already_race_sample)

    response = str(
        race.update_name(
            actual_name=actual_race_sample, new_name=already_race_sample
        )
    )

    # Cleaning DB
    race.delete(name=actual_race_sample)
    race.delete(name=already_race_sample)

    assert response == f'Error: Race {already_race_sample} already registered'
