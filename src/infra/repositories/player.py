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

    def select_one(self, id):
        try:
            data = session.query(PlayerEntity).filter(PlayerEntity.id == id)
            return data
        except Exception as exc:
            return exc
        finally:
            session.close()

    def insert(self, name, race_id, grade_id):
        try:
            data_insert = PlayerEntity(name=name, race=race_id, grade=grade_id)
            session.add(data_insert)
            session.commit()
            return data_insert
        except Exception as exc:
            return exc
        finally:
            session.close()

    def delete(self, id):
        try:
            session.query(PlayerEntity).filter(PlayerEntity.id == id).delete()
            session.commit()
            return f'Player deleted: {id}'
        except Exception as exc:
            return exc
        finally:
            session.close()

    def update(self, id, level):
        try:
            session.query(PlayerEntity).filter(PlayerEntity.id == id).update(
                {'level': level}
            )
            session.commit()
            return f'Player updated: {id}'
        except Exception as exc:
            return exc
        finally:
            session.close()
