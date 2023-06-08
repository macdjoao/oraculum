from faker import Faker

from src.infra.repositories.grade import Grade as GradeRepository

fake = Faker()
grade = GradeRepository()


def test_insert_grade():

    name = (fake.word()).capitalize()

    grade.insert(name=name)
    response = str(grade.select_one(name=name))

    assert response == f'Grade (name = {name})'


def test_delete_grade():

    name = (fake.word()).capitalize()

    grade.insert(name=name)
    response = str(grade.delete(name=name))

    assert response == f'Grade deleted: {name}'


def test_update_grade():

    actual_name = (fake.word()).capitalize()
    new_name = (fake.word()).capitalize()

    grade.insert(name=actual_name)

    update_response = str(
        grade.update(actual_name=actual_name, new_name=new_name)
    )
    select_response = str(grade.select_one(name=new_name))

    assert update_response == f'Grade updated: {new_name}'
    assert select_response == f'Grade (name = {new_name})'
