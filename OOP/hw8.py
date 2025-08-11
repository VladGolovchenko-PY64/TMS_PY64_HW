# Задание 8. Класс «Тренажёрный зал»
# Создай класс Gym.
# Требования:
# 1. Атрибуты: название зала, список клиентов (имя, возраст, абонемент активен/не
# активен).
# 2. Методы:
# o add_client(name, age) — добавить клиента.
# o remove_client(name) — удалить клиента.
# o activate_membership(name) — активировать абонемент клиента.
# o deactivate_membership(name) — деактивировать абонемент.
# o get_active_members() — вернуть список клиентов с активным абонементом.
# o find_youngest_client() — вернуть самого молодого клиента.
# o find_oldest_client() — вернуть самого старшего клиента.
# o average_age() — средний возраст клиентов.


class Gym:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def add_client(self, name, age):
        self.clients.append({"name": name, "age": age, "active": False})

    def remove_client(self, name):
        self.clients = [c for c in self.clients if c["name"] != name]

    def activate_membership(self, name):
        for client in self.clients:
            if client["name"] == name:
                client["active"] = True

    def deactivate_membership(self, name):
        for client in self.clients:
            if client["name"] == name:
                client["active"] = False

    def get_active_members(self):
        return [c for c in self.clients if c["active"]]

    def find_youngest_client(self):
        return min(self.clients, key=lambda c: c["age"], default=None)

    def find_oldest_client(self):
        return max(self.clients, key=lambda c: c["age"], default=None)

    def average_age(self):
        if not self.clients:
            return 0
        return sum(c["age"] for c in self.clients) / len(self.clients)


gym = Gym("Спорт")

gym.add_client("Иван", 25)
gym.add_client("Мария", 30)
gym.add_client("Олег", 20)

gym.activate_membership("Мария")
gym.activate_membership("Олег")

print("Активные клиенты:", gym.get_active_members())
print("Самый молодой:", gym.find_youngest_client())
print("Самый старший:", gym.find_oldest_client())
print("Средний возраст:", gym.average_age())

gym.remove_client("Иван")
print("После удаления:", gym.clients)
