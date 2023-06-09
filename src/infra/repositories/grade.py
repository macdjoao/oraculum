from src.infra.configs.session import session
from src.infra.entities.models import Grade as GradeEntity
from src.infra.repositories.errors.grade import (GradeIncompleteParamsError,
                                                 GradeNoRecordError,
                                                 GradeNotFoundError)


class Grade:
    def select_all(self):
        try:
            data = session.query(GradeEntity).all()
            if data == []:
                raise GradeNoRecordError

            return data

        except GradeNoRecordError as err:
            return err.message
        finally:
            session.close()

    def select_one(self, name: str = None):
        try:
            if name == None:
                raise GradeIncompleteParamsError(missing_param='name')

            data = (
                session.query(GradeEntity)
                .filter(GradeEntity.name == name.capitalize())
                .first()
            )
            if data == None:
                raise GradeNotFoundError(grade=name.capitalize())

            return data

        except GradeIncompleteParamsError as err:
            return err.message
        except GradeNotFoundError as err:
            return err.message
        finally:
            session.close()

    def insert(self, name: str):
        try:
            data_insert = GradeEntity(name=name.capitalize())
            session.add(data_insert)
            session.commit()
            return data_insert
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()

    def delete(self, name: str):
        try:
            session.query(GradeEntity).filter(
                GradeEntity.name == name.capitalize()
            ).delete()
            session.commit()
            return f'Grade deleted: {name}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()

    def update_name(self, actual_name: str, new_name: str):
        try:
            session.query(GradeEntity).filter(
                GradeEntity.name == actual_name.capitalize()
            ).update({'name': new_name.capitalize()})
            session.commit()
            return f'Grade updated: {new_name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()
