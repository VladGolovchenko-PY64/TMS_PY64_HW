import sqlite3
from db import DB_NAME

class TicketManager:
    @staticmethod
    def activate(user, uuid_code):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()


        cursor.execute("select available from tickets where uuid = ?", (uuid_code,))
        result = cursor.fetchone()

        if not result:
            print("Тикет не найден.")
            conn.close()
            return

        available = result[0]
        if not available:
            print("Тикет уже использован.")
            conn.close()
            return


        cursor.execute("update users set points = points + 20 where id = ?", (user["id"],))
        cursor.execute("update tickets set available = 0, user_id = ? where uuid = ?", (user["id"], uuid_code))

        conn.commit()
        conn.close()
        print("Тикет успешно активирован! Вам начислено 20 поинтов.")
