
from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, print_invoice


def main():

    while True:

        print("\n========== Coffee Shop ==========")
        print("1. Show Cafe Menu")
        print("2. Add Order")
        print("3. Show Orders")
        print("4. Calculate Total")
        print("5. Print Invoice")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                show_menu()

            case "2":
                add_order()

            case "3":
                show_orders()

            case "4":
                total = calculate_total()
                print(f"Total Amount: {total:,} Toman")

            case "5":
                print_invoice()

            case "6":
                print("Thank you for visiting our cafe!")
                break

            case _:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
