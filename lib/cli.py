from lib.models import session
from lib.models.customer import Customer
from lib.models.menu_item import MenuItem
from lib.models.order import Order

def menu():
    print("\n📋 Restaurant Order Tracker")
    print("1. View all customers")
    print("2. View all menu items")
    print("3. Create a new order")
    print("4. View all orders")
    print("5. Mark order as served")
    print("6. Exit")

def view_customers():
    customers = session.query(Customer).all()
    for c in customers:
        print(f"{c.id}: {c.name} - {c.phone}")

def view_menu_items():
    items = session.query(MenuItem).all()
    for i in items:
        print(f"{i.id}: {i.name} - ${i.price}")

def create_order():
    view_customers()
    customer_id = input("Enter customer ID: ")
    view_menu_items()
    item_id = input("Enter item ID: ")
    order = Order(customer_id=customer_id, item_id=item_id, status="pending")
    session.add(order)
    session.commit()
    print("Order created successfully!")

def view_orders():
    orders = session.query(Order).all()
    for o in orders:
        print(f"Order {o.id}: Customer {o.customer_id} | Item {o.item_id} | Status: {o.status}")

def mark_order_served():
    view_orders()
    order_id = input("Enter order ID to mark as served: ")
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        order.status = "served"
        session.commit()
        print("Order marked as served!")
    else:
        print("Order not found.")

def run():
    while True:
        menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            view_customers()
        elif choice == "2":
            view_menu_items()
        elif choice == "3":
            create_order()
        elif choice == "4":
            view_orders()
        elif choice == "5":
            mark_order_served()
        elif choice == "6":
            print(" Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run()
