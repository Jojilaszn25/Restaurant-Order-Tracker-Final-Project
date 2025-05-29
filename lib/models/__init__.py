from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///restaurant.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from .customer import Customer
from .menu_item import MenuItem
from .order import Order

__all__ = ['engine', 'Session', 'session', 'Base']
