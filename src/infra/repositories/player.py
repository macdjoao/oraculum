from src.infra.configs.session import session
from src.infra.entities.models import Player as PlayerEntity


class Player:
    def select(self):
        try:
            data = session.query(PlayerEntity).all()
            return data
        except Exception as exc:
            return exc
        finally:
            session.close()

    def insert(self, name):
        try:
            data_insert = PlayerEntity(name=name)
            session.add(data_insert)
            session.commit()
            return data_insert
        except Exception as exc:
            return exc
        finally:
            session.close()

    def delete(self, name):
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

    def update(self, name, level):
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
