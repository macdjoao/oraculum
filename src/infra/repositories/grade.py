from src.infra.configs.session import session
from src.infra.entities.models import Grade as GradeEntity


class Grade:
    def select(self):
        try:
            data = session.query(GradeEntity).all()
            return data
        except Exception as exc:
            return exc
        finally:
            session.close()

    def insert(self, name):
        try:
            data_insert = GradeEntity(name=name)
            session.add(data_insert)
            session.commit()
            return data_insert
        except Exception as exc:
            return exc
        finally:
            session.close()

    def delete(self, name):
        try:
            session.query(GradeEntity).filter(
                GradeEntity.name == name
            ).delete()
            session.commit()
            return f'Grade deleted: {name}'
        except Exception as exc:
            return exc
        finally:
            session.close()

    def update(self, actual_name, new_name):
        try:
            session.query(GradeEntity).filter(
                GradeEntity.name == actual_name
            ).update({'name': new_name})
            session.commit()
            return f'Grade updated: {id}'
        except Exception as exc:
            return exc
        finally:
            session.close()
