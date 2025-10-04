from datetime import datetime


class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id, customer, products):
        self.id = order_id
        self.customer = customer
        self.products = products
        self.total = sum(p.price for p in products)
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
