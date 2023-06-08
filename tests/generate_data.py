# Generate fake data for testing

from faker import Faker

from src.infra.repositories.grade import Grade as GradeRepository
from src.infra.repositories.player import Player as PlayerRepository
from src.infra.repositories.race import Race as RaceRepository

fake = Faker()


def generate_race(amount: int):
    data = RaceRepository()
    for i in range(amount):
        data.insert(name=fake.word())


def generate_grade(amount: int):
    data = GradeRepository()
    for i in range(amount):
        data.insert(name=fake.word())


def generate_player(amount: int, race: str, grade: str):
    data = PlayerRepository()
    for i in range(amount):
        data.insert(name=fake.first_name(), race=race, grade=grade)


# generate_race(amount=10)
# generate_grade(amount=10)
# generate_player(amount=5, race='hobbit', grade='mage')
# generate_player(amount=5, race='dwarf', grade='sorcerer')
