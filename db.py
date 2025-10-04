import json
import os
from models import Customer, Product, Order


DB_FILE = "data.json"


def load_data():
    """Загружает данные из JSON (или создаёт пустые списки)."""
    if not os.path.exists(DB_FILE):
        return [], [], []

    with open(DB_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    customers = [Customer(c["id"], c["name"], c["email"], c["phone"]) for c in data.get("customers", [])]
    products = [Product(p["id"], p["name"], p["price"]) for p in data.get("products", [])]
    orders = []

    for o in data.get("orders", []):
        cust = next((c for c in customers if c.id == o["customer_id"]), None)
        chosen_products = [next((p for p in products if p.id == pid), None) for pid in o["product_ids"]]
        chosen_products = [p for p in chosen_products if p is not None]
        if cust and chosen_products:
            orders.append(Order(o["id"], cust, chosen_products))

    return customers, products, orders


def save_data(customers, products, orders):
    """Сохраняет данные в JSON."""
    data = {
        "customers": [{"id": c.id, "name": c.name, "email": c.email, "phone": c.phone} for c in customers],
        "products": [{"id": p.id, "name": p.name, "price": p.price} for p in products],
        "orders": [
            {
                "id": o.id,
                "customer_id": o.customer.id,
                "product_ids": [p.id for p in o.products],
            }
            for o in orders
        ],
    }

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
