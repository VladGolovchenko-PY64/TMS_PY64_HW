# Создайте класс Soda (для определения типа газированной воды), принимающий
# 1 аргумент при инициализации (отвечающий за добавку к выбираемому
# лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на
# печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе
# отобразится следующая фраза: «Обычная газировка».

class Soda:
    def __init__(self, dobavka=None):
        if isinstance(dobavka, str):
            self.dobavka = dobavka
        else:
            self.dobavka = None

    def show_my_drink(self):
        if self.dobavka:
            print(f"Газировка и {self.dobavka}")
        else:
            print("Обычная газировка")


drink1 = Soda("апельсин")
drink1.show_my_drink()
