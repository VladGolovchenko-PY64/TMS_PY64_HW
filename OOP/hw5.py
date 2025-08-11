# Задание 5. Класс «Система заказов»
# Создай класс Order и класс OrderSystem.
# Order:
# • Атрибуты: номер заказа, список товаров (список словарей {"name": ..., "price":
# ..., "quantity": ...}), статус заказа.
# • Методы:
# o calculate_total() — возвращает сумму заказа.
# o add_item(name, price, quantity) — добавляет товар в заказ.
# o remove_item(name) — удаляет товар из заказа.
# o change_status(status) — изменяет статус заказа (например, «новый», «в
# работе», «завершён»).
# OrderSystem:
# • Атрибуты: список всех заказов.
# • Методы:
# o create_order() — создаёт новый заказ.
# o get_order_by_id(order_id) — возвращает заказ по номеру.
# o get_total_revenue() — возвращает общую сумму по всем завершённым
# заказам.
# o list_orders_by_status(status) — возвращает все заказы с определённым
# статусом.

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "новый"

    def calculate_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def change_status(self, status):
        self.status = status


class OrderSystem:
    def __init__(self):
        self.orders = []
        self.next_id = 1  # счётчик заказов

    def create_order(self):
        order = Order(self.next_id)
        self.orders.append(order)
        self.next_id += 1
        return order

    def get_order_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def get_total_revenue(self):
        return sum(order.calculate_total() for order in self.orders if order.status == "завершён")

    def list_orders_by_status(self, status):
        return [order for order in self.orders if order.status == status]


# Создаём систему заказов
system = OrderSystem()

# Создаём заказ
order1 = system.create_order()
order1.add_item("Телефон", 20000, 1)
order1.add_item("Чехол", 500, 2)

# Меняем статус
order1.change_status("завершён")

# Создаём второй заказ
order2 = system.create_order()
order2.add_item("Ноутбук", 80000, 1)

# Выводим общую выручку
print("Общая выручка:", system.get_total_revenue())

# Список завершённых заказов
finished_orders = system.list_orders_by_status("завершён")
for o in finished_orders:
    print(f"Заказ {o.order_id} на сумму {o.calculate_total()}")
