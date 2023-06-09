from src.infra.configs.session import session
from src.infra.entities.models import Grade as GradeEntity
from src.infra.repositories.errors.grade import (GradeAlreadyRegisteredError,
                                                 GradeIncompleteParamsError,
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

    def insert(self, name: str = None):
        try:
            if name == None:
                raise GradeIncompleteParamsError(missing_param='name')

            data_already_registered = (
                session.query(GradeEntity)
                .filter(GradeEntity.name == name.capitalize())
                .first()
            )
            if not data_already_registered == None:
                raise GradeAlreadyRegisteredError(grade=name.capitalize())

            data_insert = GradeEntity(name=name.capitalize())
            session.add(data_insert)
            session.commit()
            return data_insert

        except GradeIncompleteParamsError as err:
            session.rollback()
            return err.message
        except GradeAlreadyRegisteredError as err:
            return err.message
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

    def update_name(self, actual_name: str = None, new_name: str = None):
        try:
            if actual_name == None:
                raise GradeIncompleteParamsError(missing_param='actual_name')

            if new_name == None:
                raise GradeIncompleteParamsError(missing_param='new_name')

            data_actual_name = (
                session.query(GradeEntity)
                .filter(GradeEntity.name == actual_name.capitalize())
                .first()
            )
            if data_actual_name == None:
                raise GradeNotFoundError(grade=actual_name.capitalize())

            data_new_name = (
                session.query(GradeEntity)
                .filter(GradeEntity.name == new_name.capitalize())
                .first()
            )
            if not data_new_name == None:
                raise GradeAlreadyRegisteredError(grade=new_name.capitalize())

            session.query(GradeEntity).filter(
                GradeEntity.name == actual_name.capitalize()
            ).update({'name': new_name.capitalize()})
            session.commit()
            return f'Grade updated: {new_name.capitalize()}'

        except GradeIncompleteParamsError as err:
            session.rollback()
            return err.message
        except GradeNotFoundError as err:
            return err.message
        except GradeAlreadyRegisteredError as err:
            return err.message
        finally:
            session.close()
