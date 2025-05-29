from lib.models import session, Base, engine
from lib.models.customer import Customer
from lib.models.menu_item import MenuItem
from lib.models.order import Order

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

customer1 = Customer(name="Alice Johnson", phone="123-456-7890")
customer2 = Customer(name="Bob Smith", phone="987-654-3210")

item1 = MenuItem(name="Cheeseburger", price=8.99)
item2 = MenuItem(name="Veggie Pizza", price=10.50)
item3 = MenuItem(name="Caesar Salad", price=6.75)

session.add_all([customer1, customer2, item1, item2, item3])
session.commit()

order1 = Order(customer_id=customer1.id, item_id=item1.id, status="pending")
order2 = Order(customer_id=customer2.id, item_id=item3.id, status="served")

session.add_all([order1, order2])
session.commit()

