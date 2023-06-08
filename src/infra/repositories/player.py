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
            return exc
        finally:
            session.close()

    def update(self, name: str, level: int):
        try:
            session.query(PlayerEntity).filter(
                PlayerEntity.name == name.capitalize()
            ).update({'level': level})
            session.commit()
            return f'Player updated: {name.capitalize()}'
        except Exception as exc:
            return exc
        finally:
            session.close()
