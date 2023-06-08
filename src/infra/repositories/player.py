from src.infra.configs.session import session
from src.infra.entities.models import Player as PlayerEntity


class Player:
    def select_all(self):
        try:
            data = session.query(PlayerEntity).all()
            return data
        except Exception as exc:
            return exc
        finally:
            session.close()

    def select_one(self, name: str):
        try:
            data = (
                session.query(PlayerEntity)
                .filter(PlayerEntity.name == name.capitalize())
                .first()
            )
            return data
        except Exception as exc:
            return exc
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
