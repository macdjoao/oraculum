from src.infra.configs.session import session
from src.infra.entities.models import Player

# Insert
data_insert = Player(name='John')
session.add(data_insert)
session.commit()

# Select
data = session.query(Player).all()
print(data)

# After all
session.close()
