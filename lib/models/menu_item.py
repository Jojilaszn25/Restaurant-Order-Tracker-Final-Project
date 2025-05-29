from sqlalchemy import Column, Integer, String, Float
from lib.models import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f"<MenuItem(id={self.id}, name='{self.name}', price={self.price})>"
