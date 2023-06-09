from src.infra.configs.session import session
from src.infra.entities.models import Race as RaceEntity
from src.infra.repositories.errors.race import (RaceIncompleteParamsError,
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
            data_insert = RaceEntity(name=name.capitalize())
            session.add(data_insert)
            session.commit()
            return data_insert
        except RaceIncompleteParamsError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def delete(self, name: str):
        try:
            session.query(RaceEntity).filter(
                RaceEntity.name == name.capitalize()
            ).delete()
            session.commit()
            return f'Race deleted: {name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()

    def update_name(self, actual_name: str, new_name: str):
        try:
            session.query(RaceEntity).filter(
                RaceEntity.name == actual_name.capitalize()
            ).update({'name': new_name.capitalize()})
            session.commit()
            return f'Race updated: {new_name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()
