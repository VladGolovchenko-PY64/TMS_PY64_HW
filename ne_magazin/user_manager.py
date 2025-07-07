import sqlite3

class UserManager:
    DB = "shop.db"

    @staticmethod
    def is_exists(username: str) -> bool:
        conn = sqlite3.connect(UserManager.DB)
        cursor = conn.cursor()
        cursor.execute("select id from users where username = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    @staticmethod
    def register(username: str, password: str):
        if UserManager.is_exists(username):
            print("Пользователь с таким именем уже существует.")
            return None
        conn = sqlite3.connect(UserManager.DB)
        cursor = conn.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)", (username, password))
        conn.commit()
        conn.close()
        print("Регистрация прошла успешно.")
        return UserManager.login(username, password)

    @staticmethod
    def login(username: str, password: str):
        conn = sqlite3.connect(UserManager.DB)
        cursor = conn.cursor()
        cursor.execute("select id, username, points from users where username = ? and password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        if result:
            user = {
                "id": result[0],
                "username": result[1],
                "points": result[2]
            }
            print(f"Добро пожаловать, {user['username']}!")
            return user
        else:
            print("Неверный логин или пароль.")
            return None
