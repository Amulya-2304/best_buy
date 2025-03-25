from typing import List, Tuple
from products import Product


class Store:
    """Represents a store that manages products."""

    def __init__(self, products: List[Product]) -> None:
        """Initializes the store with a list of products."""
        self.products = products

    def add_product(self, product: Product) -> None:
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """Removes a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Processes an order and returns the total cost."""
        total_cost = sum(product.buy(quantity) for product, quantity in shopping_list)
        return total_cost


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())  # Prints total quantity of all products
    print(best_buy.order([(products[0], 1), (products[1], 2)]))  # Processes order
