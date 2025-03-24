class Product:
    """
    Represents a product in the store with attributes for name, price, quantity, and active status.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        :param name: Name of the product (must not be empty).
        :param price: Price of the product (must be non-negative).
        :param quantity: Quantity available in stock (must be non-negative).
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Updates the quantity of the product. If quantity reaches 0, deactivates the product.

        :param quantity: New quantity value (must be non-negative).
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of the product.

        :param quantity: The amount of product to buy (must be positive and within available stock).
        :return: The total price of the purchase.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


# Testing the implementation
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Should print 50 * 250
    print(mac.buy(100))  # Should print 100 * 1450
    print(mac.is_active())  # Should be False after buying all stock

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())