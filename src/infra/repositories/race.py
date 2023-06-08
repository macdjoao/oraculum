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

    def insert(self, name: str):
        try:
            data_insert = RaceEntity(name=name.capitalize())
            session.add(data_insert)
            session.commit()
            return data_insert
        except Exception as exc:
            return exc
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
            return exc
        finally:
            session.close()

    def update(self, actual_name: str, new_name: str):
        try:
            session.query(RaceEntity).filter(
                RaceEntity.name == actual_name.capitalize()
            ).update({'name': new_name.capitalize()})
            session.commit()
            return f'Race updated: {new_name.capitalize()}'
        except Exception as exc:
            return exc
        finally:
            session.close()
