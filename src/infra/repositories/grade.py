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

    def delete(self, id):
        try:
            session.query(GradeEntity).filter(GradeEntity.id == id).delete()
            session.commit()
            return f'Grade deleted: {id}'
        except Exception as exc:
            return exc
        finally:
            session.close()

    def update(self, id, name):
        try:
            session.query(GradeEntity).filter(GradeEntity.id == id).update(
                {'name': name}
            )
            session.commit()
            return f'Grade updated: {id}'
        except Exception as exc:
            return exc
        finally:
            session.close()
