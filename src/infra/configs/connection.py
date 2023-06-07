import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

engine = create_engine(SQLALCHEMY_DATABASE_URI)
