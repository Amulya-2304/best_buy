from promotions import Promotion  # Import Promotion class from promotions.py


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        # Validate product details
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
        self.promotion = None  # Added promotion attribute

    def set_promotion(self, promotion: Promotion):
        """Set promotion for the product."""
        self.promotion = promotion

    def show(self) -> str:
        """Show product details along with any active promotion."""
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        """Purchase product and apply promotion if it exists."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        # Apply promotion if exists
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price

    def set_quantity(self, quantity: int):
        """Update the product quantity."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def is_active(self) -> bool:
        """Check if the product is active based on quantity."""
        return self.quantity > 0


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)  # Quantity is 0 for non-stocked products

    def buy(self, quantity: int) -> float:
        # Since it's non-stocked, quantity doesn't affect the purchase.
        # We should apply the promotion to the price
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity  # Regular price if no promotion


class LimitedProduct(Product):
    """Class for products that have limited purchase quantity in an order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum  # Maximum quantity per purchase

    def buy(self, quantity: int) -> float:
        """Allow purchase up to the maximum quantity."""
        if quantity > self.maximum:
            raise ValueError(f"You can only buy up to {self.maximum} of this item.")
        return super().buy(quantity)
