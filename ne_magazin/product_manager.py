import sqlite3
from db import DB_NAME

class ProductManager:
    @staticmethod
    def get_available_products():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("select id, name, cost, count from products where count > 0")
        products = cursor.fetchall()
        conn.close()
        return products

    @staticmethod
    def show_products():
        products = ProductManager.get_available_products()
        if not products:
            print("Нет доступных товаров.")
            return

        print("Список товаров:")
        print("ID".ljust(5), "Название".ljust(20), "Цена".ljust(10), "Кол-во".ljust(10))
        print("-" * 50)
        for p in products:
            print(str(p[0]).ljust(5), p[1].ljust(20), str(p[2]).ljust(10), str(p[3]).ljust(10))

    @staticmethod
    def add_product():
        name = input("Название товара: ").strip()
        try:
            cost = int(input("Цена товара (в поинтах): "))
            count = int(input("Количество: "))
            if cost < 0 or count < 0:
                print("Цена и количество не могут быть отрицательными.")
                return
        except ValueError:
            print("Введите корректные числа для цены и количества.")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("insert into products (name, cost, count) values (?, ?, ?)", (name, cost, count))
        conn.commit()
        conn.close()
        print(f"Товар '{name}' добавлен.")
