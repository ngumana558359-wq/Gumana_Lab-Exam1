"""Program 2 - Inventory System: menu / entry point. Run: python main.py"""

from items import Item, PerishableItem, ElectronicItem
from inventory import Inventory


# ---------------------------- input helpers ----------------------------
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def add_item_flow(inv):
    print("Item type: 1) Regular  2) Perishable  3) Electronic")
    kind = input("Choose type: ").strip()
    if kind not in ("1", "2", "3"):
        print("Invalid type.")
        return
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    qty = read_int("Quantity: ")
    price = read_float("Price: ")
    try:
        if kind == "1":
            item = Item(name, qty, price)
        elif kind == "2":
            item = PerishableItem(name, qty, price, read_int("Days until expiry: "))
        else:
            item = ElectronicItem(name, qty, price, read_int("Warranty (months): "))
    except ValueError as e:
        print(f"Could not create item: {e}")
        return
    inv.add_item(item)


def find_or_warn(inv, name):
    item = inv.search(name)
    if item is None:
        print(f"Item '{name}' not found.")
    return item


def main():
    inv = Inventory()
    menu = """
===== INVENTORY MENU =====
1. Add item
2. Restock
3. Sell
4. Search
5. Display all items
6. Show total inventory value
7. Update quantity
8. Exit"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_item_flow(inv)
        elif choice == "2":
            item = find_or_warn(inv, input("Item name: "))
            if item:
                item.restock(read_int("Quantity to add: "))
        elif choice == "3":
            item = find_or_warn(inv, input("Item name: "))
            if item:
                item.sell(read_int("Quantity to sell: "))
        elif choice == "4":
            item = find_or_warn(inv, input("Item name: "))
            if item:
                item.display()
        elif choice == "5":
            inv.display_all()
        elif choice == "6":
            print(f"Total inventory value: {inv.total_inventory_value():.2f}")
        elif choice == "7":
            name = input("Item name: ")
            inv.update_quantity(name, read_int("New quantity: "))
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
