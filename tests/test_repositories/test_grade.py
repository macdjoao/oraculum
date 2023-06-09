from faker import Faker

from src.infra.repositories.grade import Grade as GradeRepository

fake = Faker()
grade = GradeRepository()


def test_insert_grade():

    name = (fake.word()).capitalize()

    grade.insert(name=name)
    response = str(grade.select_one(name=name))

    # Cleaning DB
    grade.delete(name=name)

    assert response == f'Grade (name = {name})'


def test_update_grade_name():

    actual_name = (fake.word()).capitalize()
    new_name = (fake.word()).capitalize()

    grade.insert(name=actual_name)

    update_response = str(
        grade.update_name(actual_name=actual_name, new_name=new_name)
    )
    select_response = str(grade.select_one(name=new_name))

    # Cleaning DB
    grade.delete(name=new_name)

    assert update_response == f'Grade updated: {new_name}'
    assert select_response == f'Grade (name = {new_name})'


def test_delete_grade():

    name = (fake.word()).capitalize()

    grade.insert(name=name)
    response = str(grade.delete(name=name))

    assert response == f'Grade deleted: {name}'


def test_grade_select_all_no_record_error():

    response = str(grade.select_all())

    assert response == 'Error: No Grade record found'


def test_grade_select_one_not_found_error():

    name = (fake.word()).capitalize()

    response = str(grade.select_one(name=name))

    assert response == f'Error: Grade {name} not found'


def test_grade_select_one_incomplete_param_error_name():

    response = str(grade.select_one())

    assert response == f'Error: Missing param "name" in Grade'
