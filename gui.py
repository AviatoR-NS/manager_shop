import tkinter as tk
from tkinter import messagebox, simpledialog
from models import Customer, Product, Order
from analysis import analyze_orders


class StoreApp:
    def __init__(self, root):
        self.customers, self.products, self.orders = [], [], []
        self.next_customer_id = self.next_product_id = self.next_order_id = 1

        self.root = root
        self.root.title("Интернет-магазин")

        # Кнопки меню
        tk.Button(root, text="Добавить клиента", command=self.register).pack(fill="x")
        tk.Button(root, text="Показать клиентов", command=self.clients).pack(fill="x")
        tk.Button(root, text="Добавить товар", command=self.add).pack(fill="x")
        tk.Button(root, text="Показать товары", command=self.show_products).pack(fill="x")
        tk.Button(root, text="Создать заказ", command=self.orders_create).pack(fill="x")
        tk.Button(root, text="Показать заказы", command=self.orders_show).pack(fill="x")
        tk.Button(root, text="Анализ заказов", command=lambda: analyze_orders(self.orders, self.text)).pack(fill="x")

        # Поле вывода
        self.text = tk.Text(root, height=20, width=80)
        self.text.pack()

    def register(self):
        name = simpledialog.askstring("Клиент", "Имя клиента:")
        email = simpledialog.askstring("Клиент", "Email:")
        phone = simpledialog.askstring("Клиент", "Телефон:")
        if not name or not email or not phone:
            return
        c = Customer(self.next_customer_id, name, email, phone)
        self.customers.append(c)
        self.next_customer_id += 1
        messagebox.showinfo("Успех", f"Клиент {c.name} добавлен!")
        self.clients()

    def clients(self):
        self.text.delete(1.0, tk.END)
        if not self.customers:
            self.text.insert(tk.END, "❌ Клиентов нет.\n")
            return
        self.text.insert(tk.END, "=== Список клиентов ===\n")
        for c in self.customers:
            self.text.insert(tk.END, f"{c.id}: {c.name}, {c.email}, {c.phone}, {c.created_at}\n")

    def add(self):
        name = simpledialog.askstring("Товар", "Название товара:")
        price = simpledialog.askfloat("Товар", "Цена товара:")
        if not name or price is None:
            return
        p = Product(self.next_product_id, name, price)
        self.products.append(p)
        self.next_product_id += 1
        messagebox.showinfo("Успех", f"Товар {p.name} добавлен!")
        self.show_products()

    def show_products(self):
        self.text.delete(1.0, tk.END)
        if not self.products:
            self.text.insert(tk.END, "❌ Товаров нет.\n")
            return
        self.text.insert(tk.END, "=== Список товаров ===\n")
        for p in self.products:
            self.text.insert(tk.END, f"{p.id}: {p.name} - {p.price} руб.\n")

    def orders_create(self):
        if not self.customers or not self.products:
            messagebox.showwarning("Ошибка", "Сначала добавьте клиентов и товары.")
            return

        cust_id = simpledialog.askinteger("Заказ", "Введите ID клиента:")
        customer = next((c for c in self.customers if c.id == cust_id), None)
        if not customer:
            messagebox.showerror("Ошибка", "Клиент не найден.")
            return

        ids = simpledialog.askstring("Заказ", "Введите ID товаров через запятую:")
        if not ids:
            return
        chosen = [p for p in self.products if p.id in map(int, ids.split(","))]

        if not chosen:
            messagebox.showerror("Ошибка", "Товары не найдены.")
            return

        o = Order(self.next_order_id, customer, chosen)
        self.orders.append(o)
        self.next_order_id += 1
        names = ", ".join(p.name for p in chosen)
        messagebox.showinfo("Успех", f"Заказ создан!\nКлиент: {customer.name}\nТовары: {names}\nСумма: {o.total} руб.")
        self.orders_show()

    def orders_show(self):
        self.text.delete(1.0, tk.END)
        if not self.orders:
            self.text.insert(tk.END, "❌ Заказов нет.\n")
            return
        self.text.insert(tk.END, "=== Список заказов ===\n")
        for o in self.orders:
            names = ", ".join(p.name for p in o.products)
            self.text.insert(tk.END, f"{o.id}: {o.customer.name} | {names} | {o.total} руб. | {o.created_at}\n")
