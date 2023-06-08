from faker import Faker

from src.infra.repositories.race import Race as RaceRepository

fake = Faker()
race = RaceRepository()


def test_insert_race():

    name = (fake.word()).capitalize()

    race.insert(name=name)
    response = str(race.select_one(name=name))

    assert response == f'Race (name = {name})'

    # Cleaning DB
    race.delete(name=name)
