"""Item classes: Item, PerishableItem, ElectronicItem."""


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.__quantity = 0
        self.__price = 0.0
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative.")
        self.__quantity = quantity
        self.__price = price

    # --- read access to the private attributes (needed by subclasses) ---
    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def set_quantity(self, qty):
        """Directly set stock level (used by Inventory.update_quantity)."""
        if qty < 0:
            print("Quantity cannot be negative.")
            return False
        self.__quantity = qty
        return True

    def restock(self, qty):
        if qty < 0:
            print("Restock rejected: quantity cannot be negative.")
            return False
        self.__quantity += qty
        print(f"Restocked {qty} x {self.name}. New quantity: {self.__quantity}")
        return True

    def sell(self, qty):
        if qty < 0:
            print("Sale rejected: quantity cannot be negative.")
            return False
        if qty > self.__quantity:
            print(f"Sale refused: only {self.__quantity} x {self.name} in stock.")
            return False
        self.__quantity -= qty
        print(f"Sold {qty} x {self.name}. Remaining: {self.__quantity}")
        return True

    def total_value(self):
        return self.__quantity * self.__price

    def display(self):
        print(f"Item: {self.name} | Qty: {self.__quantity} | "
              f"Price: {self.__price:.2f} | Total value: {self.total_value():.2f}")


class PerishableItem(Item):
    DISCOUNT = 0.5          # 50% off
    EXPIRY_THRESHOLD = 3    # days

    def __init__(self, name, quantity, price, days_until_expiry):
        super().__init__(name, quantity, price)
        self.days_until_expiry = days_until_expiry

    def is_expiring_soon(self):
        return self.days_until_expiry <= self.EXPIRY_THRESHOLD

    def total_value(self):
        value = super().total_value()
        if self.is_expiring_soon():
            value *= (1 - self.DISCOUNT)
        return value

    def display(self):
        super().display()
        note = "  (EXPIRING SOON - 50% discount applied)" if self.is_expiring_soon() else ""
        print(f"   Days until expiry: {self.days_until_expiry}{note}")


class ElectronicItem(Item):
    def __init__(self, name, quantity, price, warranty_months):
        super().__init__(name, quantity, price)
        self.warranty_months = warranty_months

    def display(self):
        super().display()
        print(f"   Warranty: {self.warranty_months} months")
