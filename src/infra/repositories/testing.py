from src.infra.configs.session import session
from src.infra.repositories.player import Player as PlayerRepository

# from src.infra.entities.models import Player as PlayerEntity

# Insert procedure
# data_insert = Player(name='Doe')
# session.add(data_insert)

# Delete procedure
# session.query(Player).filter(Player.name == 'John').delete()

# Update procedure
# session.query(Player).filter(Player.name == 'Doe').update({'level': 2})

# After every procedure
# session.commit()


# Select
# data = session.query(PlayerEntity).all()
# print(data)

# After all
# session.close()

data = PlayerRepository()
print(data.select())
