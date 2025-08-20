# Задание 2. Класс «Магазин»
# Создай класс Store, описывающий магазин.
# Требования:
# 1. Атрибуты:
# o название магазина;
# o список товаров (список словарей вида {"name": ..., "price": ...,
# "quantity": ...}).
# 2. Методы:
# o add_product(name, price, quantity) — добавить товар в магазин.
# o remove_product(name) — удалить товар по имени.
# o update_price(name, new_price) — изменить цену товара.
# o sell_product(name, quantity) — продать указанное количество товара
# (уменьшить остаток, если хватает).
# o get_inventory() — вернуть список всех товаров и их количество.
# o find_most_expensive() — вернуть самый дорогой товар.
# o find_cheapest() — вернуть самый дешёвый товар.

class OutOfStockError(Exception):
    """Ошибка: недостаточно товара на складе"""
    pass


class ProductNotFoundError(Exception):
    """Ошибка: товар не найден"""
    pass


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append({"name": name, "price": price, "quantity": quantity})

    def remove_product(self, name):
        self.products = [p for p in self.products if p["name"] != name]

    def update_price(self, name, new_price):
        for product in self.products:
            if product["name"] == name:
                product["price"] = new_price
                return True
        raise ProductNotFoundError(f"Товар '{name}' не найден для изменения цены.")

    def sell_product(self, name, quantity):
        for product in self.products:
            if product["name"] == name:
                if product["quantity"] >= quantity:
                    product["quantity"] -= quantity
                    return True
                else:
                    raise OutOfStockError(
                        f"Недостаточно товара '{name}' на складе. "
                        f"Остаток: {product['quantity']}, требуется: {quantity}"
                    )
        raise ProductNotFoundError(f"Товар '{name}' не найден для продажи.")

    def get_inventory(self):
        return [(p["name"], p["price"], p["quantity"]) for p in self.products]

    def find_most_expensive(self):
        return max(self.products, key=lambda p: p["price"], default=None)

    def find_cheapest(self):
        return min(self.products, key=lambda p: p["price"], default=None)



store = Store("Магазин")

store.add_product("Яблоки", 100, 5)
store.add_product("Бананы", 200, 10)
store.add_product("Груши", 300, 15)

print("Инвентарь:", store.get_inventory())


try:
    store.update_price("Бананы", 60)
except ProductNotFoundError as e:
    print("Ошибка:", e)


try:
    store.sell_product("Яблоки", 10)
except (OutOfStockError, ProductNotFoundError) as e:
    print("Ошибка:", e)


try:
    store.sell_product("Апельсины", 2)
except (OutOfStockError, ProductNotFoundError) as e:
    print("Ошибка:", e)

print("Самый дорогой:", store.find_most_expensive())
print("Самый дешёвый:", store.find_cheapest())

store.remove_product("Груши")
print("После удаления:", store.get_inventory())
