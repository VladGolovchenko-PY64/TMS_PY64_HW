import sqlite3
from db import DB_NAME

class OrderManager:
    @staticmethod
    def buy(user, product_id, count):
        try:
            count = int(count)
            if count <= 0:
                print("Количество должно быть больше 0.")
                return

            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()


            cursor.execute("select name, cost, count from products where id = ?", (product_id,))
            product = cursor.fetchone()
            if not product:
                print("Товар с таким ID не найден.")
                conn.close()
                return

            name, cost, available = product
            total_cost = cost * count

            if available < count:
                print(f"Недостаточно товара. В наличии: {available}")
                conn.close()
                return

            if user["points"] < total_cost:
                print(f"Недостаточно поинтов. Нужно: {total_cost}, у вас: {user['points']}")
                conn.close()
                return


            cursor.execute("insert into orders (user_id, product_id, count) values (?, ?, ?)",
                           (user["id"], product_id, count))

            cursor.execute("update products set count = count - ? where id = ?", (count, product_id))
            cursor.execute("update users set points = points - ? where id = ?", (total_cost, user["id"]))

            conn.commit()
            conn.close()
            print(f"Вы купили {count} × {name} на {total_cost} поинтов.")

        except ValueError:
            print("Неверный формат команды. Пример: купить 1 2")
