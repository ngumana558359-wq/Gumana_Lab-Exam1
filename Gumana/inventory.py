"""Inventory class: holds and manages a list of items."""


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if self.search(item.name) is not None:
            print(f"Rejected: an item named '{item.name}' already exists.")
            return False
        self.items.append(item)
        print(f"Added '{item.name}' to inventory.")
        return True

    def search(self, name):
        name = name.strip().lower()
        for item in self.items:
            if item.name.lower() == name:
                return item
        return None

    def update_quantity(self, name, qty):
        item = self.search(name)
        if item is None:
            print(f"Item '{name}' not found.")
            return False
        if item.set_quantity(qty):
            print(f"Quantity of '{item.name}' updated to {qty}.")
            return True
        return False

    def display_all(self):
        if not self.items:
            print("Inventory is empty.")
            return
        for item in self.items:
            item.display()

    def total_inventory_value(self):
        return sum(item.total_value() for item in self.items)
