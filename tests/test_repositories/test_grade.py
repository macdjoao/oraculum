from faker import Faker

from src.infra.repositories.grade import Grade as GradeRepository

fake = Faker()
grade = GradeRepository()


def test_grade_insert():

    name = (fake.word()).capitalize()

    grade.insert(name=name)
    response = str(grade.select_one(name=name))

    # Cleaning DB
    grade.delete(name=name)

    assert response == f'Grade (name = {name})'


def test_grade_update_name():

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


def test_grade_delete():

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


def test_grade_insert_incomplete_param_error_name():

    response = str(grade.insert())

    assert response == f'Error: Missing param "name" in Grade'


def test_grade_insert_already_registered_error_name():

    already_grade_name = fake.first_name()
    grade.insert(name=already_grade_name)

    response = str(grade.insert(name=already_grade_name))

    # Cleaning DB
    grade.delete(name=already_grade_name)

    assert response == f'Error: Grade {already_grade_name} already registered'


def test_grade_delete_incomplete_param_error_name():

    response = str(grade.delete())

    assert response == f'Error: Missing param "name" in Grade'


def test_grade_delete_not_found_error_name():

    name = fake.first_name()

    response = str(grade.delete(name=name))

    assert response == f'Error: Grade {name} not found'


def test_grade_update_incomplete_param_error_actual_name():

    response = str(grade.update_name())

    assert response == f'Error: Missing param "actual_name" in Grade'


def test_grade_update_incomplete_param_error_new_name():

    actual_name = fake.first_name()

    response = str(grade.update_name(actual_name=actual_name))

    assert response == f'Error: Missing param "new_name" in Grade'


def test_grade_update_not_found_error_actual_name():

    actual_name = fake.first_name()
    new_name = fake.first_name()

    response = str(
        grade.update_name(actual_name=actual_name, new_name=new_name)
    )

    assert response == f'Error: Grade {actual_name} not found'


def test_grade_update_already_registered_error_new_name():

    actual_grade_sample = fake.first_name()
    grade.insert(name=actual_grade_sample)

    already_grade_sample = fake.first_name()
    grade.insert(name=already_grade_sample)

    response = str(
        grade.update_name(
            actual_name=actual_grade_sample, new_name=already_grade_sample
        )
    )

    # Cleaning DB
    grade.delete(name=actual_grade_sample)
    grade.delete(name=already_grade_sample)

    assert (
        response == f'Error: Grade {already_grade_sample} already registered'
    )
