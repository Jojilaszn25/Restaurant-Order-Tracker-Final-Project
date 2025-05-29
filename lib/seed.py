from lib.models import Base, engine
from lib.models.customer import Customer
from lib.models.menu_item import MenuItem
from lib.models.order import Order

Base.metadata.create_all(engine)
print("Tables created!")
