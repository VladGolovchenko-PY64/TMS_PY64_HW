# Задание 7. Класс «Игровой инвентарь»
# Создай класс Inventory, представляющий инвентарь игрока.
# Требования:
# 1. Атрибуты: список предметов (каждый предмет — словарь с полями name, weight,
# value).
# 2. Методы:
# o add_item(name, weight, value) — добавить предмет.
# o remove_item(name) — удалить предмет.
# o get_total_weight() — вернуть общий вес.
# o get_total_value() — вернуть общую стоимость.
# o find_heaviest() — найти самый тяжёлый предмет.
# o find_most_valuable() — найти самый дорогой предмет.
# o sort_by_value() — вернуть предметы, отсортированные по стоимости.
# o sort_by_weight() — вернуть предметы, отсортированные по весу.


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, weight, value):
        self.items.append({"name": name, "weight": weight, "value": value})

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False

    def get_total_weight(self):
        return sum(item["weight"] for item in self.items)

    def get_total_value(self):
        return sum(item["value"] for item in self.items)

    def find_heaviest(self):
        return max(self.items, key=lambda x: x["weight"], default=None)

    def find_most_valuable(self):
        return max(self.items, key=lambda x: x["value"], default=None)

    def sort_by_value(self):
        return sorted(self.items, key=lambda x: x["value"], reverse=True)

    def sort_by_weight(self):
        return sorted(self.items, key=lambda x: x["weight"], reverse=True)

inv = Inventory()
inv.add_item("Меч", 5, 300)
inv.add_item("Щит", 7, 200)
inv.add_item("Кольцо", 1, 500)

print("Общий вес:", inv.get_total_weight())
print("Общая стоимость:", inv.get_total_value())
print("Самый тяжёлый:", inv.find_heaviest())
print("Самый дорогой:", inv.find_most_valuable())

print("Сортировка по цене:", inv.sort_by_value())
print("Сортировка по весу:", inv.sort_by_weight())

inv.remove_item("Щит")
print("После удаления:", inv.items)
