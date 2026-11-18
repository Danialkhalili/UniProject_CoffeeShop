
menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000,
    "juice": 90000,
    "sandwich": 150000
}


def show_menu():
    print("\n========== Cafe Menu ==========")

    for product, price in menu.items():
        print(f"{product} : {price:,} Toman")

    print("===============================")
