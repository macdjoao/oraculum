from src.infra.configs.session import session
from src.infra.entities.models import Race as RaceEntity


class Race:
    def select(self):
        try:
            data = session.query(RaceEntity).all()
            return data
        except Exception as exc:
            return exc
        finally:
            session.close()

    def insert(self, name):
        try:
            data_insert = RaceEntity(name=name)
            session.add(data_insert)
            session.commit()
            return data_insert
        except Exception as exc:
            return exc
        finally:
            session.close()

    def delete(self, id):
        try:
            session.query(RaceEntity).filter(RaceEntity.id == id).delete()
            session.commit()
            return f'Race deleted: {id}'
        except Exception as exc:
            return exc
        finally:
            session.close()

    def update(self, id, name):
        try:
            session.query(RaceEntity).filter(RaceEntity.id == id).update(
                {'name': name}
            )
            session.commit()
            return f'Race updated: {id}'
        except Exception as exc:
            return exc
        finally:
            session.close()
