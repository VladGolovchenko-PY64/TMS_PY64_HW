import sqlite3
from db import DB_NAME

class ProfileManager:
    @staticmethod
    def show_profile(user):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        print(f"\n Профиль пользователя: {user['username']}")

        # Получаем поинты
        cursor.execute("select points from users where id = ?", (user["id"],))
        points = cursor.fetchone()[0]
        print(f"Поинты: {points}")

        # Получаем заказы
        cursor.execute('''
            select products.name, products.cost, orders.count
            from orders
            join products on orders.product_id = products.id
            where orders.user_id = ?
        ''', (user["id"],))

        orders = cursor.fetchall()

        if not orders:
            print("У вас пока нет покупок.")
        else:
            print("\n История покупок:")
            print("Товар".ljust(20), "Цена".ljust(10), "Кол-во".ljust(10))
            print("-" * 45)
            for name, cost, count in orders:
                print(name.ljust(20), str(cost).ljust(10), str(count).ljust(10))

        conn.close()
