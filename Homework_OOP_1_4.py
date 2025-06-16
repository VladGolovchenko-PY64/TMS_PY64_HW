# Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString.

class RealString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        return len(self) == len(other) if isinstance(other, RealString) else len(self) == len(other)

    def __ne__(self, other):
        return len(self) != len(other) if isinstance(other, RealString) else len(self) != len(other)

    def __lt__(self, other):
        return len(self) < len(other) if isinstance(other, RealString) else len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other) if isinstance(other, RealString) else len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other) if isinstance(other, RealString) else len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other) if isinstance(other, RealString) else len(self) >= len(other)


a = RealString("Йежик")
b = RealString("Страус")

print(a > b)
print(a < b)
print(a == "Носорог")