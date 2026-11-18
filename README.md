# Coffee Shop Management System

## Project Description
This is a simple Python project for managing coffee shop orders.

The program allows users to view the cafe menu, add orders, display orders, calculate the total price, and print the final invoice.

## Project Structure

```text
coffee_shop/
│
├── Main.py
├── Menu.py
├── Order.py
├── Billing.py
└── README.md
```

## Features

- Show the coffee shop menu.
- Add new orders.
- Display all registered orders.
- Calculate the total price.
- Calculate a 10% discount for orders over 1,000,000 Toman.
- Print the final invoice.
- Exit the program.

## Discount Rules

If the total order price is more than 1,000,000 Toman, the customer gets a 10% discount.

Otherwise, no discount is applied.

## Notes

- All orders are stored in memory.
- Orders are deleted when the program is closed.
- No external libraries are required.

## Author

Created as a Python programming course project.
