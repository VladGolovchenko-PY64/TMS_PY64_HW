# Задание 1. Класс «Игровой персонаж»
# Создай класс GameCharacter, который описывает персонажа игры.
# Требования:
# 1. У персонажа есть имя, здоровье и уровень.
# 2. Здоровье хранится в приватном атрибуте.
# 3. Сделай property для здоровья, чтобы при попытке установить здоровье выше 100 оно
# автоматически становилось 100.
# 4. Сделай защищённый метод _level_up(), который увеличивает уровень на 1.
# 5. Добавь метод attack(other_character), который уменьшает здоровье другого
# персонажа на 10.
# 6. Сделай classmethod, который создаёт персонажа с максимальным здоровьем (100) и
# уровнем 1.
# 7. Сделай staticmethod, который сравнивает двух персонажей по уровню и возвращает
# того, у кого уровень выше.

class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.__health = health
        self.level = level

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 100:
            self.__health = 100
        elif value < 0:
            self.__health = 0
        else:
            self.__health = value

    def _level_up(self):
        self.level += 1

    def attack(self, other_character):
        other_character.health -= 10

    @classmethod
    def create_default(cls, name):
        return cls(name, 100, 1)

    @staticmethod
    def compare_levels(char1, char2):
        return char1 if char1.level > char2.level else char2

# создание перса
hero1 = GameCharacter.create_default("Нуб")
hero2 = GameCharacter("Враг", 80, 2)

# Атака
hero1.attack(hero2)
print(hero2.health)  # 70

# Повышение уровня
hero1._level_up()
print(hero1.level)  # 2

# Сравнение по уровню
winner = GameCharacter.compare_levels(hero1, hero2)
print(f"Более сильный по уровню: {winner.name}")
