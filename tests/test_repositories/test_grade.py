from faker import Faker

from src.infra.repositories.grade import Grade as GradeRepository

fake = Faker()
grade = GradeRepository()


def test_insert_grade():

    fake_name = (fake.word()).capitalize()

    grade.insert(name=fake_name)
    response = str(grade.select_one(name=fake_name))

    assert response == f'Grade (name = {fake_name})'


def test_delete_grade():

    fake_name = (fake.word()).capitalize()

    grade.insert(name=fake_name)
    response = str(grade.delete(name=fake_name))

    assert response == f'Grade deleted: {fake_name}'
