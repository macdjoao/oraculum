from sqlalchemy.orm import sessionmaker

from .connection import engine

Session = sessionmaker(bind=engine)
session = Session()
