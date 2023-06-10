from src.infra.configs.session import session
from src.infra.entities.models import Grade as GradeEntity
from src.infra.entities.models import Player as PlayerEntity
from src.infra.entities.models import Race as RaceEntity
from src.infra.repositories.errors.grade import GradeNotFoundError
from src.infra.repositories.errors.player import (PlayerAlreadyRegisteredError,
                                                  PlayerIncompleteParamsError,
                                                  PlayerLevelNotIntError,
                                                  PlayerNoRecordError,
                                                  PlayerNotFoundError)
from src.infra.repositories.errors.race import RaceNotFoundError


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

    def insert(self, name: str = None, race: str = None, grade: str = None):
        try:
            if name == None:
                raise PlayerIncompleteParamsError(missing_param='name')
            if race == None:
                raise PlayerIncompleteParamsError(missing_param='race')
            if grade == None:
                raise PlayerIncompleteParamsError(missing_param='grade')

            race_not_found = (
                session.query(RaceEntity)
                .filter(RaceEntity.name == race.capitalize())
                .first()
            )
            if race_not_found == None:
                raise RaceNotFoundError(race=race.capitalize())

            grade_not_found = (
                session.query(GradeEntity)
                .filter(GradeEntity.name == grade.capitalize())
                .first()
            )
            if grade_not_found == None:
                raise GradeNotFoundError(grade=grade.capitalize())

            data_already_registered = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == name.capitalize())
                .first()
            )
            if not data_already_registered == None:
                raise PlayerAlreadyRegisteredError(player=name.capitalize())

            data_insert = PlayerEntity(
                name=name.capitalize(),
                race=race.capitalize(),
                grade=grade.capitalize(),
            )
            session.add(data_insert)
            session.commit()
            return data_insert

        except PlayerIncompleteParamsError as err:
            session.rollback()
            return err.message
        except PlayerAlreadyRegisteredError as err:
            session.rollback()
            return err.message
        except RaceNotFoundError as err:
            session.rollback()
            return err.message
        except GradeNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def delete(self, name: str = None):
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

            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).delete()
            session.commit()
            return f'Player deleted: {name.capitalize()}'

        except PlayerIncompleteParamsError as err:
            session.rollback()
            return err.message
        except PlayerNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def update_name(self, actual_name: str = None, new_name: str = None):
        try:
            if actual_name == None:
                raise PlayerIncompleteParamsError(missing_param='actual_name')

            if new_name == None:
                raise PlayerIncompleteParamsError(missing_param='new_name')

            data = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == actual_name.capitalize())
                .first()
            )
            if data == None:
                raise PlayerNotFoundError(player=actual_name.capitalize())

            data_new_name = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == new_name.capitalize())
                .first()
            )
            if not data_new_name == None:
                raise PlayerAlreadyRegisteredError(
                    player=new_name.capitalize()
                )

            session.query(PlayerEntity).filter(
                PlayerEntity.name == actual_name.capitalize()
            ).update({'name': new_name.capitalize()})
            session.commit()
            return f'Player updated: {new_name.capitalize()}'

        except PlayerIncompleteParamsError as err:
            session.rollback()
            return err.message
        except PlayerNotFoundError as err:
            session.rollback()
            return err.message
        except PlayerAlreadyRegisteredError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def update_level(self, name: str = None, level: int = None):
        try:
            if name == None:
                raise PlayerIncompleteParamsError(missing_param='name')

            if level == None:
                raise PlayerIncompleteParamsError(missing_param='level')

            if not isinstance(level, int):
                raise PlayerLevelNotIntError

            data = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == name.capitalize())
                .first()
            )
            if data == None:
                raise PlayerNotFoundError(player=name.capitalize())

            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).update({'level': level})
            session.commit()
            return f'Player updated: {name.capitalize()}'

        except PlayerIncompleteParamsError as err:
            session.rollback()
            return err.message
        except PlayerLevelNotIntError as err:
            session.rollback()
            return err.message
        except PlayerNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def update_race(self, name: str = None, race: str = None):
        try:
            if name == None:
                raise PlayerIncompleteParamsError(missing_param='name')

            if race == None:
                raise PlayerIncompleteParamsError(missing_param='race')

            data = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == name.capitalize())
                .first()
            )
            if data == None:
                raise PlayerNotFoundError(player=name.capitalize())

            race_not_found = (
                session.query(RaceEntity)
                .filter(RaceEntity.name == race.capitalize())
                .first()
            )
            if race_not_found == None:
                raise RaceNotFoundError(race=race.capitalize())

            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).update({'race': race.capitalize()})
            session.commit()
            return f'Player updated: {name.capitalize()}'

        except PlayerIncompleteParamsError as err:
            session.rollback()
            return err.message
        except PlayerNotFoundError as err:
            session.rollback()
            return err.message
        except RaceNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def update_grade(self, name: str = None, grade: str = None):
        try:
            if name == None:
                raise PlayerIncompleteParamsError(missing_param='name')

            if grade == None:
                raise PlayerIncompleteParamsError(missing_param='grade')

            data = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == name.capitalize())
                .first()
            )
            if data == None:
                raise PlayerNotFoundError(player=name.capitalize())

            grade_not_found = (
                session.query(GradeEntity)
                .filter(GradeEntity.name == grade.capitalize())
                .first()
            )
            if grade_not_found == None:
                raise GradeNotFoundError(grade=grade.capitalize())

            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).update({'grade': grade.capitalize()})
            session.commit()
            return f'Player updated: {name.capitalize()}'

        except PlayerIncompleteParamsError as err:
            session.rollback()
            return err.message
        except PlayerNotFoundError as err:
            session.rollback()
            return err.message
        except GradeNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()
