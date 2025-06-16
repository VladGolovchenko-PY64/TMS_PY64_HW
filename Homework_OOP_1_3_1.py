# Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы: - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),  - get_kg() - для вывода текущего значения кг.
# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.

class KgToPounds:
    def __init__(self, kg):
        self._kg = kg if isinstance(kg, (int, float)) else 0

    def to_pounds(self):
        return self._kg * 2.205

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, value):
        if isinstance(value, (int, float)):
            self._kg = value
        else:
            print("Ошибка: нужно ввести число.")


obj = KgToPounds(100)
print(obj.to_pounds())

obj.kg = 10
print(obj.kg)

obj.kg = "10"
print(obj.kg) 