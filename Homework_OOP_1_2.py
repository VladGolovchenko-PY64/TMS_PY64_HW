# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от
# ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if not all(isinstance(side, (int, float)) for side in self.sides):
            return "Нужно вводить только числа!"


        if not all(side > 0 for side in self.sides):
            return "С отрицательными числами ничего не выйдет!"


        if len(self.sides) != 3:
            return "Жаль, но из этого треугольник не сделать."

        a, b, c = sorted(self.sides)
        if a + b > c:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

x1 = TriangleChecker([3, 4, 5])
print(x1.is_triangle())

x2 = TriangleChecker([1, 2, 3])
print(x2.is_triangle())

x3 = TriangleChecker([3, -4, 5])
print(x3.is_triangle())

x4 = TriangleChecker([1, "xxxxx", 3])
print(x4.is_triangle())
