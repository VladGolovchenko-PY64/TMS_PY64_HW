# Задание 6. Класс «Автомобиль»
# Создай класс Car, описывающий автомобиль.
# Требования:
# 1. Атрибуты: марка, модель, год, уровень топлива (в литрах), пробег.
# 2. Методы:
# o drive(distance) — увеличить пробег и уменьшить топливо (расход 0.1 л на 1
# км).
# o refuel(liters) — заправить автомобиль.
# o info() — вывести состояние автомобиля.
# o __check_fuel() (приватный) — проверяет, хватит ли топлива для поездки.
# o age() (метод экземпляра) — возвращает возраст автомобиля.
# 3. classmethod from_string(cls, data) — создаёт объект из строки вида "Toyota,
# Corolla, 2015".

from datetime import datetime

class Car:
    def __init__(self, brand, model, year, fuel=0, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        self.mileage = mileage

    def drive(self, distance):
        if self.__check_fuel(distance):
            self.mileage += distance
            self.fuel -= distance * 0.1
            print(f"Проехали {distance} км. Остаток топлива: {self.fuel:.1f} л")
        else:
            print("Недостаточно топлива для поездки!")

    def refuel(self, liters):
        self.fuel += liters
        print(f"Заправлено {liters} л. Теперь в баке {self.fuel} л")

    def info(self):
        print(f"{self.brand} {self.model}, {self.year} г.")
        print(f"Пробег: {self.mileage} км, Топливо: {self.fuel:.1f} л")

    def __check_fuel(self, distance):
        needed = distance * 0.1
        return self.fuel >= needed

    def age(self):
        current_year = datetime.now().year
        return current_year - self.year

    @classmethod
    def from_string(cls, data):
        brand, model, year = map(str.strip, data.split(","))
        return cls(brand, model, int(year))


# Создаём авто
car1 = Car.from_string("Toyota, Corolla, 2015")
car1.refuel(20)
car1.info()

# Поездка
car1.drive(50)
car1.info()

# Возраст
print("Возраст авто:", car1.age(), "лет")
