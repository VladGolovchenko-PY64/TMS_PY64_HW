# Задание 1
# Напишите функцию make_sentence, которая принимает один именованный
# аргумент words, который должен быть списком строк, и возвращает строку,
# составленную из элементов списка, разделенных пробелами и
# заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию
# используется список ["This", "is", "a", "sentence"].
# Решение.

def make_sentence(words=None):
    if words is None:
        words = ["This", "is", "a", "sentence"]
    return " ".join(words) + "."

print(make_sentence())
print(make_sentence(["Hello", "World"]))

# Задание 2
# Напишите функцию sum_of_squares, которая принимает произвольное
# количество позиционных аргументов, которые должны быть числами, и
# возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0.
# Решение.

def sum_of_squares(*args):
    for x in args:
        if not isinstance(x, int):
            print("Это не целые числа!")
            return 0
    return sum(x ** 2 for x in args)

print(sum_of_squares(1, 2, 3, 4, 5))
print(sum_of_squares(1, 2, 3.25, 4, 5))

# Задание 3
# Напишите функцию greet, которая принимает два именованных аргумента:
# name и language. Аргумент name должен быть строкой, а аргумент language
# должен быть одним из трех возможных значений: "en", "ru" или "fr".
# Функция должна возвращать приветствие на выбранном языке.
# Если аргумент language не указан, то по умолчанию используется "en".
# Решение.

def greet(name, language="en"):
    if not isinstance(name, str):
        return "Имя не строка!"

    greetings = {
        "en": f"Hello, {name}!",
        "ru": f"Привет, {name}!",
        "fr": f"Bonjour, {name}!"
    }

    if language not in greetings:
        return "Язык должен быть 'en', 'ru' или 'fr'."

    return greetings[language]

print(greet("Vlad"))
print(greet("Юля", language="ru"))
print(greet("Tom", language="fr"))
print(greet("John", language="blr"))

# Задание 4
# Напишите функцию print_info, которая принимает произвольное
# количество именованных аргументов (**kwargs) и выводит их в формате
# "key: value" по одной паре на строку. Напоминаю, что kwargs в функции
# будет словарем. Если функции не передано ни одного аргумента, она должна
# вывести "No info given.".
# Решение.

def print_info(**kwargs):
    if not kwargs:
        print("No info given.")
    else:
        for key, value in kwargs.items():
            print(f"{key}: {value}")

print_info(name="Alex", age=25, city="Amsterdam")
print_info()

# Задание 5
# Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".
# Решение.

def print_table(**kwargs):
    if not kwargs:
        print("No data given.")
    else:
        print(f"| {'Key':<10} | {'Value':<10} |")
        print(f"|", "-" * 23, "|")
        for key, value in kwargs.items():
            print(f"| {key:<10} | {value:<10} |")

print_table(name="Bob", age=30, city="Amsterdam")
print_table()

# Задание 6
# Напишите функцию calculate, которая принимает произвольное количество
# позиционных аргументов, которые должны быть числами, и один
# именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/".
# Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи.
# Если функции не передано ни одного позиционного аргумента, она должна
# вернуть 0.
# Если аргумент operation не указан, то по умолчанию используется "+".
# Решение.

def calculate(*args, operation="+"):
    if not args:
        return 0

    if operation not in ["+", "-", "*", "/"]:
        return "Неизвестная операция!"

    result = args[0]
    for num in args[1:]:
        if operation == "+":
            result += num
        elif operation == "-":
            result -= num
        elif operation == "*":
            result *= num
        elif operation == "/":
            if num == 0:
                return "Деление на ноль!"
            result /= num
    return result

print(calculate(1, 2, 3))
print(calculate(1, 2, 3, operation="-"))
print(calculate(1, 0, operation="/"))
print(calculate(1, 2, operation="%"))

# Задание 7
# Напишите функцию print_triangle, которая принимает один именованный
# аргумент height, который должен быть положительным целым числом, и
# выводит равнобедренный треугольник из символов "*" с заданной высотой.
# Если аргумент height не указан, то по умолчанию используется число 5.
# Решение.

def print_triangle(height=5):
    if not isinstance(height, int) or height <= 0:
        print("Высота должна быть положительным целым числом.")
        return

    for i in range(1, height + 1):
        stars = "*" * (2 * i - 1)
        print(f"{stars:^{2 * height - 1}}")

print_triangle(height=6)

# Задание 8
# Напишите функцию create_post, которая создает пост для блога,
# основываясь на переданных параметрах. Обязательными параметрами
# являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет
# текущая значение “general”. Функция должна возвращать словарь поста.
# Решение.

def create_post(title, content, author, category="general"):
    post = {
        "title": title,
        "content": content,
        "author": author,
        "category": category
    }

    for key, value in post.items():
        print(f"{key}: {value}")

    return post

create_post("Муха", "Насекомое с крыльями. Жужжит.", "Влад", category="Вечерний бред")
create_post("Муха", "Насекомое с крыльями. Жужжит.", "Влад")

# Задание 9
# Напишите функцию create_product, которая создает товар для интернет
# магазина, основываясь на переданных параметрах. Обязательными
# параметрами являются: имя, цена и категория. Необязательным параметром
# является рейтинг. Если он не был передан параметр, то по умолчанию будет
# 0. Функция должна возвращать словарь товара.
# Решение.

def create_product(name, price, category, rating=0.0):
    product = {
        "name": name,
        "price": price,
        "category": category,
        "rating": rating
    }
    for key, value in product.items():
        print(f"{key}: {value}")
    return product

p = create_product("Ноутбук", 999999, "Электроника", rating=4.8)
p1 = create_product("Ноутбук", 11111, "Электроника")

# Задание 10
# Напишите функцию create_student, которая создает словарь студента
# для учебного заведения, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, фамилия, отчество и группа.
# Также дополнительными параметрами могут быть: дата поступления в виде
# строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес.
# Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть
# в словаре.
# Решение.

def create_student(first_name, last_name, middle_name, group, **kwargs):
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name,
        "group": group
    }
    for key, value in kwargs.items():
        student[key] = value

    for key, value in student.items():
        print(f"{key}: {value}")

    return student

student1 = create_student("Иван",
                          "Иванов",
                          "Иванович",
                          "БИ-2",
                          date_start="19.10.2023",
                          sr_ball=3.2,
                          semestr=1,
                          phone_number="+375291234567",
                          adress="Belarus, Brest")