from lib.models import session
from lib.models.customer import Customer
from lib.models.menu_item import MenuItem
from lib.models.order import Order
import csv

def get_valid_input(prompt, valid_options):
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        print("Invalid option. Try again.")

def view_customers():
    customers = session.query(Customer).all()
    for c in customers:
        print(f"{c.id}: {c.name} - {c.phone}")

def view_menu_items():
    items = session.query(MenuItem).all()
    for i in items:
        print(f"{i.id}: {i.name} - ${i.price:.2f}")

def create_order():
    view_customers()
    customer_id = input("Enter customer ID: ")
    view_menu_items()
    item_id = input("Enter menu item ID: ")
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
    order = session.query(Order).get(order_id)
    if order:
        order.status = "served"
        session.commit()
        print("Order marked as served!")
    else:
        print("Order not found.")

def search_customer():
    name = input("Enter customer name to search: ").lower()
    customers = session.query(Customer).filter(Customer.name.ilike(f"%{name}%")).all()
    if customers:
        for c in customers:
            print(f"{c.id}: {c.name} - {c.phone}")
    else:
        print("No customers found.")

def filter_orders_by_status():
    status = input("Enter order status to filter by (pending/served): ").lower()
    orders = session.query(Order).filter(Order.status == status).all()
    if orders:
        for o in orders:
            print(f"Order {o.id}: Customer {o.customer_id} | Item {o.item_id} | Status: {o.status}")
    else:
        print(f"No orders found with status '{status}'.")

def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    customer = Customer(name=name, phone=phone)
    session.add(customer)
    session.commit()
    print("Customer added successfully!")

def export_orders_to_csv():
    orders = session.query(Order).all()
    with open("orders_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Order ID", "Customer ID", "Item ID", "Status"])
        for o in orders:
            writer.writerow([o.id, o.customer_id, o.item_id, o.status])
    print("Orders exported to orders_export.csv")

def menu():
    print("\n📋 Restaurant Order Tracker")
    print("1. View all customers")
    print("2. View all menu items")
    print("3. Create a new order")
    print("4. View all orders")
    print("5. Mark order as served")
    print("6. Search customer by name")
    print("7. Filter orders by status")
    print("8. Add new customer")
    print("9. Export orders to CSV")
    print("0. Exit")

def run():
    while True:
        menu()
        choice = get_valid_input("\nChoose an option: ", [str(i) for i in range(10)])
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
            search_customer()
        elif choice == "7":
            filter_orders_by_status()
        elif choice == "8":
            add_customer()
        elif choice == "9":
            export_orders_to_csv()
        elif choice == "0":
            print("Exiting...")
            break

if __name__ == "__main__":
    run()
