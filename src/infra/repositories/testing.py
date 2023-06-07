from src.infra.configs.session import session
from src.infra.entities.models import Player

# Insert
# data_insert = Player(name='Doe')
# session.add(data_insert)
# session.commit()

# Delete
# session.query(Player).filter(Player.name == 'John').delete()
# session.commit()

# Update
session.query(Player).filter(Player.name == 'Doe').update({'level': 2})
session.commit()

# Select
data = session.query(Player).all()
print(data)

# After all
session.close()
