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
                .filter(PlayerEntity.name == name)
                .first()
            )
            return data
        except Exception as exc:
            return exc
        finally:
            session.close()

    def insert(self, name: str, race: str, grade: str):
        try:
            data_insert = PlayerEntity(name=name, race=race, grade=grade)
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
                PlayerEntity.name == name
            ).delete()
            session.commit()
            return f'Player deleted: {name}'
        except Exception as exc:
            return exc
        finally:
            session.close()

    def update(self, name: str, level: int):
        try:
            session.query(PlayerEntity).filter(
                PlayerEntity.name == name
            ).update({'level': level})
            session.commit()
            return f'Player updated: {name}'
        except Exception as exc:
            return exc
        finally:
            session.close()
