# Задание 4. Класс «Кошелёк»
# Создай класс Wallet, описывающий электронный кошелёк.
# Требования:
# 1. Приватный атрибут _balance.
# 2. Методы:
# o deposit(amount) — пополнить кошелёк.
# o withdraw(amount) — снять деньги (если хватает).
# o transfer_to(other_wallet, amount) — перевести деньги другому кошельку.
# o __apply_bonus() (приватный метод) — добавить 1% бонуса к балансу,
# вызывается автоматически после каждой операции пополнения.
# 3. property balance — позволяет просматривать баланс.
# 4. Статический метод wallet_info(wallet) — выводит краткую информацию о
# кошельке.

class InvalidAmountError(Exception):
    """Ошибка: сумма должна быть положительной"""
    pass


class InsufficientFundsError(Exception):
    """Ошибка: недостаточно средств на счёте"""
    pass


class Wallet:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise InvalidAmountError("Начальный баланс не может быть отрицательным!")
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__apply_bonus()
        else:
            raise InvalidAmountError("Сумма для пополнения должна быть положительной!")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Сумма для снятия должна быть положительной!")
        if amount > self._balance:
            raise InsufficientFundsError("Недостаточно средств для снятия!")
        self._balance -= amount

    def transfer_to(self, other_wallet, amount):
        if amount <= 0:
            raise InvalidAmountError("Сумма для перевода должна быть положительной!")
        if amount > self._balance:
            raise InsufficientFundsError("Недостаточно средств для перевода!")
        self._balance -= amount
        other_wallet.deposit(amount)

    def __apply_bonus(self):  # Приватный метод: добавляет 1% бонуса
        bonus = self._balance * 0.01
        self._balance += bonus

    @staticmethod
    def wallet_info(wallet):
        print(f"Баланс кошелька: {wallet.balance:.2f}")



try:
    w1 = Wallet(100)
    w2 = Wallet(200)


    w1.deposit(500)
    Wallet.wallet_info(w1)


    w1.withdraw(300)
    Wallet.wallet_info(w1)


    w1.transfer_to(w2, 200)
    Wallet.wallet_info(w1)
    Wallet.wallet_info(w2)


    w1.withdraw(1000)
except (InvalidAmountError, InsufficientFundsError) as e:
    print("Ошибка:", e)
