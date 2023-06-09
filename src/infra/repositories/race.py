from src.infra.configs.session import session
from src.infra.entities.models import Race as RaceEntity
from src.infra.repositories.errors.race import (RaceAlreadyRegisteredError,
                                                RaceIncompleteParamsError,
                                                RaceNoRecordError,
                                                RaceNotFoundError)


class Race:
    def select_all(self):
        try:
            data = session.query(RaceEntity).all()
            if data == []:
                raise RaceNoRecordError

            return data

        except RaceNoRecordError as err:
            return err.message
        finally:
            session.close()

    def select_one(self, name: str = None):
        try:
            if name == None:
                raise RaceIncompleteParamsError(missing_param='name')

            data = (
                session.query(RaceEntity)
                .filter(RaceEntity.name == name.capitalize())
                .first()
            )
            if data == None:
                raise RaceNotFoundError(race=name.capitalize())

            return data

        except RaceIncompleteParamsError as err:
            return err.message
        except RaceNotFoundError as err:
            return err.message
        finally:
            session.close()

    def insert(self, name: str = None):
        try:
            if name == None:
                raise RaceIncompleteParamsError(missing_param='name')

            data_already_registered = (
                session.query(RaceEntity)
                .filter(RaceEntity.name == name.capitalize())
                .first()
            )
            if not data_already_registered == None:
                raise RaceAlreadyRegisteredError(race=name.capitalize())

            data_insert = RaceEntity(name=name.capitalize())
            session.add(data_insert)
            session.commit()
            return data_insert

        except RaceIncompleteParamsError as err:
            session.rollback()
            return err.message
        except RaceAlreadyRegisteredError as err:
            return err.message
        finally:
            session.close()

    def delete(self, name: str = None):
        try:
            if name == None:
                raise RaceIncompleteParamsError(missing_param='name')

            session.query(RaceEntity).filter(
                RaceEntity.name == name.capitalize()
            ).delete()
            session.commit()
            return f'Race deleted: {name.capitalize()}'

        except RaceIncompleteParamsError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def update_name(self, actual_name: str = None, new_name: str = None):
        try:
            if actual_name == None:
                raise RaceIncompleteParamsError(missing_param='actual_name')

            if new_name == None:
                raise RaceIncompleteParamsError(missing_param='new_name')

            data_actual_name = (
                session.query(RaceEntity)
                .filter(RaceEntity.name == actual_name.capitalize())
                .first()
            )
            if data_actual_name == None:
                raise RaceNotFoundError(race=actual_name.capitalize())

            data_new_name = (
                session.query(RaceEntity)
                .filter(RaceEntity.name == new_name.capitalize())
                .first()
            )
            if not data_new_name == None:
                raise RaceAlreadyRegisteredError(race=new_name.capitalize())

            session.query(RaceEntity).filter(
                RaceEntity.name == actual_name.capitalize()
            ).update({'name': new_name.capitalize()})
            session.commit()
            return f'Race updated: {new_name.capitalize()}'

        except RaceIncompleteParamsError as err:
            session.rollback()
            return err.message
        except RaceNotFoundError as err:
            return err.message
        except RaceAlreadyRegisteredError as err:
            return err.message
        finally:
            session.close()
