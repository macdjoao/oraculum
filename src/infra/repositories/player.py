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
