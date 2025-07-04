# Задание 1
# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий только четные числа из исходного списка. Используйте функцию
# filter и лямбда-выражение.
#Решение.

numbers = list(map(int, input("Введите числа через пробел: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Четные числа:", even_numbers)

# Задание 2
# Напишите код, который принимает список кортежей вида (имя, возраст) и
# возвращает новый список, отсортированный по возрастанию возраста.
# Используйте функцию sorted и ключ сортировки.
#Решение.

data = [
    ("Саша", 99),
    ("Петя", 33),
    ("Вася", 22),
    ("Оля", 10)
]
sorted_data = sorted(data, key=lambda x: x[1])
print("Отсортированный список:")
for name, age in sorted_data:
    print(f"{name} - {age} лет")

# Задание 3
# Напишите код, который принимает список строк и возвращает новый список,
# содержащий только те строки, которые начинаются с гласной буквы. (Да да,
# снова эти гласные) Используйте функцию filter и множество.
#Решение.

vowels = set("aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ")
user_input = input("Введите слова через пробел: ")
words = user_input.split()
filtered_words = list(filter(lambda word1: word1[0] in vowels, words))
print("Слова, начинающиеся с гласной буквы:")
for word in filtered_words:
    print(word)

# Задание 4
# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте функцию map и lambda.
#Решение.

user_input = input("Введите числа через пробел: ")
kvadrat = list(map(lambda x: int(x)**2, user_input.split()))
print(kvadrat)

# Задание 5
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по убыванию длины слов. Используйте функцию sorted и
# обратный порядок сортировки.
#Решение.

words = input("Введите слова через пробел: ").split()
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)

# Задание 6
# Напишите код, который принимает строку и возвращает список, содержащий
# только те буквы, которые встречаются в слове “python”. Используйте функцию
# filter и оператор in.
#Решение.

user_input = input("Введите строку: ")
letters = list(filter(lambda x: x in "python", user_input))
print(letters)

# Задание 7
# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий эти же числа, умноженные на 10. Используйте функцию.
#Решение.

def x_by_10(numbers1):
    return [num * 10 for num in numbers1]

user_input = input("Введите числа через пробел: ")
numbers = list(map(int, user_input.split()))
print(x_by_10(numbers))

# Задание 8
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по алфавиту. Используйте функцию sorted.
#Решение.

words = input("Введите слова через пробел: ").split()
print(sorted(words))

# Задание 9
# Напишите функцию, которая принимает список строк и возвращает новый
# список, содержащий только те строки, которые являются палиндромами.
# Палиндром — это слово, которое читается одинаково слева направо и справа
# налево. Используйте функцию filter и сравнение строк.
#Решение.

def filter_palindromes(words):
    return list(filter(lambda w: w == w[::-1], words))
words = ["00100", "привет", "шалаш", "12321", "python"]
palindromes = filter_palindromes(words)
print(palindromes)


# Задание 10
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества гласных букв в словах.
# Используйте функцию sorted и ключ сортировки.
#Решение.

vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"

def count_vowels(word):
    return sum(1 for x in word if x in vowels)

words = ["яблоко", "груша", "вишня", "клубника", "носки"]
sorted_words = sorted(words, key=count_vowels)
print(sorted_words)

# Задание 11
# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки в верхнем регистре. Используйте функцию map и
# встроенный метод строк upper.
#Решение.

words = ["стена", "лампа", "яблоко"]
upper_words = list(map(str.upper, words))
print(upper_words)

# Задание 12
# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки с добавленным префиксом “Hello”. Используйте
# функцию map и конкатенацию строк.
#Решение.

words = ["One", "Two", "Three"]
greetings = list(map(lambda x: "Hello_" + x, words))
print(greetings)

# Задание 13
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества букв “a” в словах. Используйте
# функцию sorted и ключ сортировки.
#Решение.

words = input("Введите слова через пробел: ").split()
sorted_words = sorted(words, key=lambda word: word.lower().count('a'))
print(sorted_words)

# Задание 14
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества уникальных букв в словах.
# Используйте функцию sorted и ключ сортировки.
#Решение.

words = input("Введите слова через пробел: ").split()
sorted_words = sorted(words, key=lambda word: len(set(filter(str.isalpha, word.lower()))))
print(sorted_words)

# Задание 15
# Напишите декоратор retry_five, который повторяет вызов декорируемой
# функции 5 раз.
#Решение.

def retry_five(func):

    def wrapper(*args, **kwargs):
        print("Begin:")
        for i in range(5):
            res = func(*args, **kwargs)
        print("End:")
        return res

    return wrapper


@retry_five
def print_text():
    print("Текст")

print(print_text())

