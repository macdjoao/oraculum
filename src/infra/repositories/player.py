from src.infra.configs.session import session
from src.infra.entities.models import Player as PlayerEntity
from src.infra.repositories.errors.player import (PlayerIncompleteParamsError,
                                                  PlayerNoRecordError,
                                                  PlayerNotFoundError)


class Player:
    def select_all(self):
        try:
            data = session.query(PlayerEntity).all()
            if data == []:
                raise PlayerNoRecordError

            return data

        except PlayerNoRecordError as err:
            return err.message
        finally:
            session.close()

    def select_one(self, name: str = None):
        try:
            if name == None:
                raise PlayerIncompleteParamsError(missing_param='name')

            data = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == name.capitalize())
                .first()
            )
            if data == None:
                raise PlayerNotFoundError(player=name.capitalize())

            return data

        except PlayerIncompleteParamsError as err:
            return err.message
        except PlayerNotFoundError as err:
            return err.message
        finally:
            session.close()

    def insert(self, name: str, race: str, grade: str):
        try:
            data_insert = PlayerEntity(
                name=name.capitalize(),
                race=race.capitalize(),
                grade=grade.capitalize(),
            )
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
            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).delete()
            session.commit()
            return f'Player deleted: {name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()

    def update_name(self, actual_name: str, new_name: str):
        try:
            session.query(PlayerEntity).filter(
                PlayerEntity.name == actual_name.capitalize()
            ).update({'name': new_name.capitalize()})
            session.commit()
            return f'Player updated: {new_name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()

    def update_level(self, name: str, level: int):
        try:
            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).update({'level': level})
            session.commit()
            return f'Player updated: {name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()

    def update_race(self, name: str, race: str):
        try:
            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).update({'race': race.capitalize()})
            session.commit()
            return f'Player updated: {name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()

    def update_grade(self, name: str, grade: str):
        try:
            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).update({'grade': grade.capitalize()})
            session.commit()
            return f'Player updated: {name.capitalize()}'
        except Exception as exc:
            session.rollback()
            return exc
        finally:
            session.close()
