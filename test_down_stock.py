from Entities.Product import Product

def test_down_stock():
    product1 = Product(4, "Noodle", 5.98, 6)

    # Act
    product1.down_stock(2)

    # Assert
    assert product1.get_stock() == 4