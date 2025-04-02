import unittest
from products import Product, NonStockedProduct, LimitedProduct


class TestProduct(unittest.TestCase):
    """Test cases for Product class."""

    def test_normal_product_creation(self):
        """Test that creating a normal product works."""
        p = Product("MacBook Air M2", 1450, 100)
        self.assertEqual(p.name, "MacBook Air M2")
        self.assertEqual(p.price, 1450)
        self.assertEqual(p.quantity, 100)
        self.assertTrue(p.active)
        self.assertIsNone(p.promotion)

    def test_product_creation_empty_name(self):
        """Test that creating a product with an empty name raises an exception."""
        with self.assertRaises(ValueError):
            Product("", 1450, 100)

    def test_product_creation_negative_price(self):
        """Test that creating a product with a negative price raises an exception."""
        with self.assertRaises(ValueError):
            Product("MacBook Air M2", -10, 100)

    def test_product_creation_negative_quantity(self):
        """Test that creating a product with a negative quantity raises an exception."""
        with self.assertRaises(ValueError):
            Product("MacBook Air M2", 1450, -5)

    def test_product_becomes_inactive_when_quantity_zero(self):
        """Test that when a product reaches 0 quantity, it becomes inactive."""
        p = Product("Test Product", 100, 10)
        p.buy(10)  # Purchasing all available units
        self.assertEqual(p.quantity, 0)
        self.assertFalse(p.active)

    def test_product_purchase_reduces_quantity_and_returns_correct_total(self):
        """Test that a product purchase reduces the quantity and returns correct total."""
        p = Product("Test Product", 100, 20)
        total = p.buy(5)
        self.assertEqual(total, 500)   # 5 * 100 = 500
        self.assertEqual(p.quantity, 15)

    def test_product_purchase_exact_total_price(self):
        """Test that purchasing a specific quantity returns the expected total price."""
        p = Product("Test Product", 100, 10)
        total = p.buy(3)
        self.assertEqual(total, 300)   # 3 * 100 = 300

    def test_product_purchase_exceeding_quantity(self):
        """Test that buying a larger quantity than available invokes an exception."""
        p = Product("Test Product", 100, 5)
        with self.assertRaises(ValueError):
            p.buy(6)

    def test_product_purchase_invalid_quantity_zero(self):
        """Test that purchasing 0 quantity raises an exception."""
        p = Product("Test Product", 100, 10)
        with self.assertRaises(ValueError):
            p.buy(0)

    def test_multiple_purchases_reduce_quantity_and_deactivate(self):
        """Test multiple purchases reduce quantity and deactivate when reaching 0."""
        p = Product("Test Product", 50, 50)
        total1 = p.buy(10)
        total2 = p.buy(15)
        total3 = p.buy(25)  # This purchase should bring the quantity to 0.
        self.assertEqual(total1, 500)      # 10 * 50
        self.assertEqual(total2, 750)      # 15 * 50
        self.assertEqual(total3, 1250)     # 25 * 50
        self.assertEqual(p.quantity, 0)
        self.assertFalse(p.active)
        # Now, trying to purchase further should raise an exception.
        with self.assertRaises(ValueError):
            p.buy(1)


class TestNonStockedProduct(unittest.TestCase):
    """Test cases for NonStockedProduct class."""

    def test_non_stocked_product_creation(self):
        """Test that creating a non-stocked product works."""
        p = NonStockedProduct("Warranty", 100)
        self.assertEqual(p.name, "Warranty")
        self.assertEqual(p.price, 100)
        self.assertEqual(p.quantity, 0)
        self.assertTrue(p.active)

    def test_non_stocked_product_buy(self):
        """Test that buying a non-stocked product works with any quantity."""
        p = NonStockedProduct("Warranty", 100)
        total = p.buy(1000)  # Should work despite quantity being 0
        self.assertEqual(total, 100000)  # 1000 * 100
        self.assertEqual(p.quantity, 0)  # Quantity remains 0


class TestLimitedProduct(unittest.TestCase):
    """Test cases for LimitedProduct class."""

    def test_limited_product_creation(self):
        """Test that creating a limited product works."""
        p = LimitedProduct("Special Edition", 200, 50, 2)
        self.assertEqual(p.name, "Special Edition")
        self.assertEqual(p.price, 200)
        self.assertEqual(p.quantity, 50)
        self.assertEqual(p.maximum, 2)
        self.assertTrue(p.active)

    def test_limited_product_buy_within_limit(self):
        """Test that buying a limited product within limit works."""
        p = LimitedProduct("Special Edition", 200, 50, 2)
        total = p.buy(2)  # Within limit
        self.assertEqual(total, 400)  # 2 * 200
        self.assertEqual(p.quantity, 48)

    def test_limited_product_buy_exceeds_limit(self):
        """Test that buying a limited product exceeding limit raises exception."""
        p = LimitedProduct("Special Edition", 200, 50, 2)
        with self.assertRaises(ValueError):
            p.buy(3)  # Exceeds limit of 2


if __name__ == '__main__':
    unittest.main()