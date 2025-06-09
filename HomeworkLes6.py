# Задание 1.
# Напишите функцию, которая принимает на вход строку (предложение), а возвращает самое длинное слово из строки.
# def longest_word(text):
#    pass
# Решение
def longest_word(text):
    words = text.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

user_input = input("Введите предложение: ")
result = longest_word(user_input)
print("Самое длинное слово:", result)

# Задание 2.
# Напишите функцию, которая принимает на вход строку и заменяет в ней все множественные пробелы на одинарные.
#       Например: 'Hello,    world' -> 'Hello, world'
# def replace_multiple_spaces(text):
#    pass
# Решение
def replace_multiple_spaces(text):
    words = text.split()
    result = ""

    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:
            result += " "

    return result

user_input = input("Введите текст с множественными пробелами: ")
print("Текст после замены множественных пробелов:", replace_multiple_spaces(user_input))

# Задание 3.
# Напишите функцию, которая принимает на вход строку и возвращает словарь,
# где ключи - это символы, а значения - количество этих символов в строке.
#       Например: 'Hello, world!' -> {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
#       Подсказка: используйте метод строки `count("a")`, который возвращает количество вхождений символа в строку.
# def count_letters(text):
#    pass
# Решение
def count_letters(text):
    result = {}
    for char in text:
        if char not in result:
            result[char] = text.count(char)
    return result

user_input = input("Введите строку: ")
print(count_letters(user_input))

# Задание 4.
# Напишите функцию, которая принимает на вход строку и возвращает True,
# если строка является палиндромом, и False - в противном случае.
#       Палиндром - это строка, которая читается одинаково в обоих направлениях.
#       Например: 'мадам', 'А роза упала на лапу Азора'
#def is_palindrome(text):
#    pass
# Решение
def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

user_input = input("Введите строку: ")
print(is_palindrome(user_input))


# Задание 5.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку,
#       в которой все символы, которые не являются буквами, удалены (пробел разрешен).
#       Например: 'Hello, world!' -> 'Hello world'
#       Подсказка: используйте цикл и метод строки `isalpha()` для проверки, является ли символ буквой.
# def remove_non_letters(text):
#    pass
# Решение

def remove_non_letters(text):
    result = ""
    for char in text:
        if char.isalpha() or char == " ":
            result += char
    return result

user_input = input("Введите строку: ")
print(remove_non_letters(user_input))


# Задание 6.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку,
# в которой все гласные буквы заменены на символ '*'.
# def replace_vowels(text):
#    pass
# Решение
def replace_vowels(text):
    let_const = "аеёиоуыэюяaeiou"
    result = ""
    for char in text:
        if char.lower() in let_const:
            result += "*"
        else:
            result += char
    return result

user_input = input("Введите строку: ")
print(replace_vowels(user_input))


# Задание 7.
# Напишите функцию, которая принимает на вход число и возвращает сумму его цифр.
# def sum_digits(number):
#    pass
# Решение
def sum_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

num = input("Введите число: ")
result = sum_digits(num)
print("Сумма цифр числа:", result)



# Задание 8.
# Напишите функцию, которая принимает на вход число и возвращает True,
# если число является степенью двойки, и False - в противном случае.
#       Например: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536 и т.д.
#       Подсказка: используйте цикл и оператор деления без остатка.
# def is_power_of_two(number):
#    pass
# Решение

def is_power_of_two(number):
    if number < 1:
        return False
    while number % 2 == 0:
        number = number // 2
    return number == 1

num = int(input("Введите число: "))
print("Это степень двойки?", is_power_of_two(num))


# Задание 9.
# Напишите функцию, которая принимает на вход три целых числа и возвращает True,
# если они могут быть длинами сторон треугольника.
#       Подсказка: сумма двух сторон треугольника должна быть больше третьей стороны.
# def is_triangle(a, b, c):
#    pass
# Решение
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

a = int(input("Введите сторону a: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))

if is_triangle(a, b, c):
    print("Это треугольник.")
else:
    print("Это не треугольник.")


# Задание 10.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку, в которой все символы,
# которые встречаются более одного раза, заменены на символ '_'.
# def replace_duplicates(text):
#    pass
# Решение

def replace_duplicates(text):
    result = ""
    for char in text:
        if text.count(char) > 1:
            result += "_"
        else:
            result += char
    return result

user_input = input("Введите строку: ")
print("Результат:", replace_duplicates(user_input))