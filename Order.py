
from Menu import menu


orders = []


def add_order():
    product = input("Enter product name: ").lower()

    if product not in menu:
        print("This product is not available!")
        return

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return

    order = {
        "product": product,
        "price": menu[product],
        "quantity": quantity
    }

    orders.append(order)

    print("Order added successfully!")


def show_orders():
    if len(orders) == 0:
        print("No orders have been registered!")
        return

    print("\n========== Your Orders ==========")

    for order in orders:
        print(f"Product: {order['product']}")
        print(f"Price: {order['price']:,} Toman")
        print(f"Quantity: {order['quantity']}")
        print("---------------------------------")
