from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount


class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity >= 2:
            full_price_items = quantity // 2
            half_price_items = quantity - full_price_items
            total_price = (full_price_items * product.price) + (half_price_items * product.price / 2)
            return total_price
        else:
            return product.price * quantity


class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        total_price = (quantity - free_items) * product.price
        return total_price
