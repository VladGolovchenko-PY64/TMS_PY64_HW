from user_manager import UserManager
from product_manager import ProductManager
from order_manager import OrderManager
from ticket_manager import TicketManager
from profile_manager import ProfileManager


current_user = None

def main():
    global current_user

    while True:
        print("\n=== Главное меню ===")
        print("1. Зарегистрироваться")
        print("2. Войти")
        print("3. Посмотреть товары")
        print("4. Купить товар")
        print("5. Активировать тикет")
        print("6. Профиль")
        print("7. Добавить товар")
        print("0. Выйти")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            username = input("Логин: ")
            password = input("Пароль: ")
            current_user = UserManager.register(username, password)

        elif choice == "2":
            username = input("Логин: ")
            password = input("Пароль: ")
            current_user = UserManager.login(username, password)

        elif choice == "3":
            ProductManager.show_products()

        elif choice == "4":
            if current_user is None:
                print("Сначала войдите в аккаунт.")
                continue
            prod_id = input("Введите ID товара: ")
            qty = input("Введите количество: ")
            OrderManager.buy(current_user, prod_id, qty)


        elif choice == "5":

            if current_user is None:
                print("Сначала войдите в аккаунт.")

                continue

            uuid_code = input("Введите UUID тикета: ")

            TicketManager.activate(current_user, uuid_code)



        elif choice == "6":

            if current_user is None:
                print("Сначала войдите в аккаунт.")

                continue

            ProfileManager.show_profile(current_user)

        elif choice == "7":
            if current_user is None:
                print("Сначала войдите в аккаунт.")
                continue

            ProductManager.add_product()

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неизвестный пункт. Введите число от 0 до 6.")

if __name__ == "__main__":
    from db import create_tables, clear_data, seed_tickets

    create_tables()
    # clear_data()
    seed_tickets()
    main()
