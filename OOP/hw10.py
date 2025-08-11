# Задание 10. Класс «Учебная группа»
# Цель: объединение нескольких объектов в один класс-менеджер.
# Описание:
# Создай класс Student и класс StudyGroup.
# Student:
# • Атрибуты: имя, оценки (список чисел).
# • Методы:
# o add_grade(grade) — добавить оценку.
# o average_grade() — вернуть среднюю оценку.
# o info() — вывести информацию об ученике.
# StudyGroup:
# • Атрибуты: название группы, список студентов.
# • Методы:
# o add_student(student) — добавить ученика.
# o remove_student(name) — удалить ученика по имени.
# o find_best_student() — найти ученика с лучшей средней оценкой.
# o group_average() — средняя оценка по группе.
# o list_students() — вывести список всех студентов.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def info(self):
        print(f"Имя: {self.name}, Средняя оценка: {self.average_grade():.2f}")


class StudyGroup:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def find_best_student(self):
        return max(self.students, key=lambda s: s.average_grade(), default=None)

    def group_average(self):
        if not self.students:
            return 0
        return sum(s.average_grade() for s in self.students) / len(self.students)

    def list_students(self):
        print(f"Список студентов группы {self.name}:")
        for s in self.students:
            s.info()


# Создаём студентов
s1 = Student("Вася")
s2 = Student("Маша")
s3 = Student("Петя")

# Добавляем оценки
s1.add_grade(5)
s1.add_grade(4)
s2.add_grade(3)
s2.add_grade(4)
s3.add_grade(5)
s3.add_grade(5)

# Создаём группу
group = StudyGroup("Python-разработчики")
group.add_student(s1)
group.add_student(s2)
group.add_student(s3)

# Выводим всех студентов
group.list_students()

# Лучшая средняя оценка
best = group.find_best_student()
print(f"Лучший студент: {best.name}, средняя: {best.average_grade():.2f}")

# Средняя по группе
print(f"Средняя оценка по группе: {group.group_average():.2f}")
