# Задание 1

# Имеется структура данных пользователя.

# Уменьшите день рождения пользователя на 1 день.
# Измените язык пользователя на "ru".
# Измените тему на "dark".
# Измените статус активности на "false".
# Добавьте новую запись в историю активности пользователя.

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
    "preferences": {
        "language": "fr",
        "theme": "light",
        "notifications": {
            "email": False,
            "sms": True,
            "push": True
        },
        "privacy": {
            "showOnlineStatus": True,
            "profileVisibility": "public"
        }
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

# Решение:

# Уменьшите день рождения пользователя на 1 день
birthDate_str = user1["profile"]["birthDate"]
print(birthDate_str)
date_parts = list(map(int, birthDate_str.split("-")))
print(date_parts)
date_parts[2] = date_parts[2] - 1
print(date_parts)
new_birth = str(date_parts[0]) + "-" + str(date_parts[1]) + "-" + str(date_parts[2])
print(new_birth)
user1["profile"]["birthDate"] = new_birth
print(user1)

# Измените язык пользователя на "ru"
user1["preferences"]["language"] = "ru"

# Измените тему на "dark"
user1["preferences"]["theme"] = "dark"

# Измените статус активности на "false"
user1["accountStatus"]["isActive"] = False

# Добавьте новую запись в историю активности пользователя
new_activitylog = {
    "timestamp": "2025-05-19T21:01:12Z",
    "activity": "Updated profile settings"
}
user1["activityLogs"].append(new_activitylog)


