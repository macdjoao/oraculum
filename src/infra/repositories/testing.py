from src.infra.configs.session import session
from src.infra.entities.models import Player

# Insert procedure
# data_insert = Player(name='Doe')
# session.add(data_insert)

# Delete procedure
# session.query(Player).filter(Player.name == 'John').delete()

# Update procedure
# session.query(Player).filter(Player.name == 'Doe').update({'level': 2})

# After every procedure
session.commit()


# Select
data = session.query(Player).all()
print(data)

# After all
session.close()
