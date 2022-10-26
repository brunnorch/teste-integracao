from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository


def test_sale():
    # Arrange
    customer1 = Customer(1, "João")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(3, "Rice", 10.23, 9)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 3)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert order.total_price == 30.69



