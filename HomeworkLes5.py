# Задание 1
# Через цикл вывести в консоль все элементы списка.
# Используя цикл, вывести в консоль все элементы списка в обратном порядке.
# Используя цикл, вывести в консоль все элементы списка, а их буквы в обратном порядке.
# list1 = ['apple', 'banana', 'cherry']
# Решение
list1 = ['apple', 'banana', 'cherry']
print("Все элементы списка:")
for item in list1:
    print(item)
print("Элементы списка в обратном порядке:")
for item in reversed(list1):
    print(item)
print("Элементы списка, буквы в обратном порядке:")
for item in list1:
    print(item[::-1])

# Задание 2
# Используя цикл, вывести в консоль все ключи словаря.
# Используя цикл, вывести в консоль все ключи и значения словаря.
# dict1 = {
#    "name": "John",
#    "age": 30,
#    "city": "New York"
# }
# Решение
dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Ключи словаря:")
for key in dict1:
    print(key)
print("Ключи и значения словаря:")
for key in dict1:
    print(key, ":", dict1[key])

# Задание 3
# На вход пользователь вводит целое число (использовать функцию input).
# Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно.
# Используя цикл, вывести в консоль все числа от введенного числа до 1 включительно.
# Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно, которые делятся на 3 без остатка.
# Решение
# Пользователь вводит целое число
num = int(input("Введите целое число: "))
print("Числа от 1 до", num)
for i in range(1, num + 1):
    print(i)
print("Числа от", num, "до 1")
for i in range(num, 0, -1):
    print(i)
print("Числа от 1 до", num, "которые делятся на 3:")
for i in range(1, num + 1):
    if i % 3 == 0:
        print(i)

# Задание 4
# На вход пользователь вводит предложение (использовать функцию input).
# Посчитайте количество слов в предложении и выведите результат в консоль.
# Используя цикл, выведите в консоль все слова предложения в обратном порядке.
# Используя цикл, создайте словарь, где ключами являются длина слов,
# а значениями - список слов в предложении с такой длиной.
# Решение
user_input = input("Введите предложение: ")
words = user_input.split()
print("Количество слов в предложении:", len(words))
print("Слова в обратном порядке:")
for word in reversed(words):
    print(word)
length_dict = {}
for word in words:
    length = len(word)
    if length not in length_dict:
        length_dict[length] = []
    length_dict[length].append(word)
print("Итоговый Словарь: ")
print(length_dict)

# Задание 5
# На вход пользователь должен ввести username, email, имя и фамилию по очереди (использовать функцию input).
# Для каждого параметра: если введенные данные не соответствуют требованиям
# (например, username должен быть длиной от 3 до 20 символов),
# выведите сообщение об ошибке и попросите ввести данные заново.
# Создайте словарь с данными пользователя и выведите его в консоль.
# Решение

while True:
    username = input("Введите username (от 3 до 20 символов): ")
    if 3 <= len(username) <= 20:
        break
    else:
        print("Ошибка: username должен быть от 3 до 20 символов.")
while True:
    email = input("Введите email: ")
    if "@" in email and "." in email:
        break
    else:
        print("Ошибка: некорректный email. Должен содержать '@' и '.'")
while True:
    first_name = input("Введите имя: ")
    if first_name.isalpha():
        break
    else:
        print("Ошибка: имя должно содержать только буквы.")
while True:
    last_name = input("Введите фамилию: ")
    if last_name.isalpha():
        break
    else:
        print("Ошибка: фамилия должна содержать только буквы.")
user_data = {
    "username": username,
    "email": email,
    "first_name": first_name,
    "last_name": last_name
}
print(user_data)

# Задание 6*
# Напишите в коде случайное число от 1 до 100.
# Пользователь должен угадать это число.
# Используя цикл, попросите пользователя ввести число до тех пор, пока он не угадает.
# Если пользователь ввел не число, выведите сообщение "Вы ввели не число".
# Если пользователь ввел число, которое не попало в диапазон от 1 до 100, выведите сообщение "Число не входит в диапазон от 1 до 100".
# Если пользователь ввел число больше загаданного, выведите сообщение "Загаданное число меньше".
# Если пользователь ввел число меньше загаданного, выведите сообщение "Загаданное число больше".
# Если пользователь угадал число, выведите сообщение "Вы угадали!" и завершите программу.
# Решение

secret_number = 99
while True:
    user_input = input("Введите число от 1 до 100: ")
    if not user_input.isdigit():
        print("Вы ввели не число.")
        continue

    user_input = int(user_input)

    if user_input < 1 or user_input > 100:
        print("Число не входит в диапазон от 1 до 100.")
        continue

    if user_input < secret_number:
        print("Загаданное число больше.")
    elif user_input > secret_number:
        print("Загаданное число меньше.")
    else:
        print("Вы угадали!")
        break

# Задание 7*
# Имеется структура данных пользователя.

# Используя цикл, выведите все активности по логам пользователя в консоль со временем и описанием.
# Если пользователь активен, выведите сообщение "Пользователь активен", иначе выведите "Пользователь не активен".
# Если у пользователя есть аватар, то выведите его в консоль, если нет, то выведите "Нет аватара".


user1 = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    },
    "accountStatus": {
        "isActive": True,
        "lastLogin": "2025-01-10T09:15:00Z",
        "createdAt": "2023-03-20T11:00:00Z"
    },
    "activityLogs": [
        {
            "timestamp": "2025-01-09T18:30:00Z",
            "activity": "Commented on a post"
        },
        {
            "timestamp": "2025-01-08T16:45:00Z",
            "activity": "Liked a post"
        }
    ]
}

# Решение
print("Активности пользователя:")
for log in user1["activityLogs"]:
    print(log["timestamp"] + ": " + log["activity"])
if user1["accountStatus"]["isActive"]:
    print("Пользователь активен")
else:
    print("Пользователь не активен")
avatar = user1["profile"].get("avatarUrl")
if avatar:
    print("Аватар пользователя: " + avatar)
else:
    print("Нет аватара")

# Задание 8*

# Имеется структура данных продукта.

# Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов товара на складе.
# Выведите через цикл все варианты товара на складе в виде строки в формате: "Название - цена (кол-во на складе)".
# Используя цикл, найдите вариант товара с максимальной ценой и выведите его название и цену в консоль.
# Выведите через цикл все отзывы о товаре в виде строки в формате: "Пользователь - Оценка - Комментарий".
# Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
# Через цикл выведите только названия файлов картинок (например, "main.jpg" и "side.jpg") товара в консоль.
# Используя цикл, найдите и выведите в консоль все отзывы пользователя с именем "techguy123".

product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 0
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 198.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },
        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}

# Решение
total_quantity = 0
for variant in product1["variants"]:
    total_quantity += variant["stockQuantity"]
product1["stock"]["quantity"] = total_quantity
print("Варианты товара:")
for variant in product1["variants"]:
    print(variant["color"] + " - " + str(variant["price"]) + " (" + str(variant["stockQuantity"]) + ")")
max_variant = product1["variants"][0]
max_price = max_variant["price"]
for variant in product1["variants"]:
    if variant["price"] > max_price:
        max_price = variant["price"]
        max_variant = variant
print("Вариант с максимальной ценой:")
print(max_variant["color"] + " - " + str(max_variant["price"]))
print("Отзывы о товаре:")
for review in product1["reviews"]:
    print(review["username"] + " - " + str(review["rating"]) + " - " + review["comment"])
count_5 = 0
for review in product1["reviews"]:
    if review["rating"] == 5:
        count_5 += 1
print("Количество отзывов с оценкой 5:", count_5)
print("Файлы изображений:")
for url in product1["images"]:
    print(url.split("/")[-1])
print("Отзывы от пользователя techguy123:")
for review in product1["reviews"]:
    if review["username"] == "techguy123":
        print(review["username"] + " - " + str(review["rating"]) + " - " + review["comment"])