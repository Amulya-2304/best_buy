import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


# Test 1: Test creating a product with promotion
def test_create_product_with_promotion():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    promotion = PercentDiscount("30% off!", percent=30)
    product.set_promotion(promotion)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.promotion.name == "30% off!"


# Test 2: Test applying percentage discount promotion
def test_apply_percent_discount():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    promotion = PercentDiscount("30% off!", percent=30)
    product.set_promotion(promotion)

    total_price = product.buy(1)
    expected_price = 1450 * 0.7  # 30% off
    # Use pytest.approx to allow a small margin of error
    assert total_price == pytest.approx(expected_price, rel=1e-9)


# Test 3: Test applying second item at half price promotion
def test_apply_second_half_price():
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    promotion = SecondHalfPrice("Second Half price!")
    product.set_promotion(promotion)

    total_price = product.buy(2)  # Buy two items
    expected_price = 250 + 125  # First item full price, second item half price
    assert total_price == expected_price


# Test 4: Test applying "Buy 2, get 1 free" promotion
def test_apply_third_one_free():
    product = Product("Google Pixel 7", price=500, quantity=250)
    promotion = ThirdOneFree("Third One Free!")
    product.set_promotion(promotion)

    total_price = product.buy(3)  # Buy 3 items, pay for 2
    expected_price = 500 * 2  # Only pay for 2 items
    assert total_price == expected_price


# Test 5: Test NonStockedProduct with promotion (should not be allowed to buy more than 1)


# Test 6: Test LimitedProduct with promotion (should not exceed max quantity per purchase)
def test_limited_product_buy_with_promotion():
    product = LimitedProduct("Shipping Fee", price=10, quantity=250, maximum=1)
    promotion = SecondHalfPrice("Second Half price!")
    product.set_promotion(promotion)

    with pytest.raises(ValueError):
        product.buy(2)  # Trying to buy more than the maximum allowed quantity

    total_price = product.buy(1)  # Buy within limit
    expected_price = 10  # No discount for a single item
    assert total_price == expected_price


# Test 7: Test applying no promotion (should just buy normally)
def test_apply_no_promotion():
    product = Product("Google Pixel 7", price=500, quantity=250)
    total_price = product.buy(1)
    expected_price = 500  # No discount, normal price
    assert total_price == expected_price


# Test 8: Test show method to check product with promotion details
def test_show_product_with_promotion():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    promotion = PercentDiscount("30% off!", percent=30)
    product.set_promotion(promotion)

    show_info = product.show()
    assert "Promotion: 30% off!" in show_info

