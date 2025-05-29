from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    item_id = Column(Integer, ForeignKey('menu_items.id'))
    status = Column(String, default='pending')

    customer = relationship("Customer", backref="orders")
    item = relationship("MenuItem")

    def __repr__(self):
        return f"<Order(id={self.id}, customer={self.customer.name}, item={self.item.name}, status={self.status})>"
