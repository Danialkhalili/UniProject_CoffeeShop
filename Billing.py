
from Order import orders


def calculate_total():
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total


def calculate_discount(total):
    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount


def print_invoice():
    if len(orders) == 0:
        print("No orders to print!")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final_price = total - discount

    print("\n========== INVOICE ==========")

    for order in orders:
        print(
            f"{order['product']} "
            f"x {order['quantity']} "
            f"= {order['price'] * order['quantity']:,} Toman"
        )

    print("-----------------------------")
    print(f"Total: {total:,.0f} Toman")
    print(f"Discount: {discount:,.0f} Toman")
    print(f"Final Price: {final_price:,.0f} Toman")
    print("=============================")
