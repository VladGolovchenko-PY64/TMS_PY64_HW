# Четное или нечетное?
# Напишите программу, которая определяет, является число четным или
# нечетным.
# Ввод:
# 132
# Вывод:
# Четно

# Решение:

# Считываем число

user = int(input())
words = {
        0: "Введенное число - Четное",
        1: "Введенное число - Нечетное"
}
print(words[user % 2])
