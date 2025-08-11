# Задание 3. Класс «Библиотека» и класс «Книга»
# Создай два класса: Book и Library.
# Book:
# • Атрибуты: название, автор, год издания, статус (в библиотеке или выдана).
# • Метод info() — выводит информацию о книге.
# • Метод mark_as_taken() — меняет статус на «выдана».
# • Метод mark_as_returned() — меняет статус на «в библиотеке».
# Library:
# • Атрибуты: название библиотеки, список книг.
# • Методы:
# o add_book(book) — добавляет книгу в библиотеку.
# o remove_book(book) — удаляет книгу из библиотеки.
# o find_by_author(author) — находит все книги автора.
# o find_by_year(year) — находит все книги указанного года.
# o available_books() — возвращает список всех книг, которые в библиотеке.
# o taken_books() — возвращает список всех выданных книг.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "в библиотеке"

    def info(self):
        return f"{self.title} — {self.author}, {self.year} ({self.status})"

    def mark_as_taken(self):
        self.status = "выдана"

    def mark_as_returned(self):
        self.status = "в библиотеке"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def find_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def find_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def available_books(self):
        return [book for book in self.books if book.status == "в библиотеке"]

    def taken_books(self):
        return [book for book in self.books if book.status == "выдана"]


# Создаём книги
book1 = Book("Война и мир", "Толстой", 1869)
book2 = Book("Преступление и наказание", "Достоевский", 1866)
book3 = Book("Мастер и Маргарита", "Булгаков", 1967)

# Создаём библиотеку
library = Library("Городская библиотека")

# Добавляем книги
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Выдаём одну книгу
book2.mark_as_taken()

# Поиск
print("Книги Толстого:")
for b in library.find_by_author("Толстой"):
    print(b.info())

print("\nКниги 1869 года:")
for b in library.find_by_year(1869):
    print(b.info())

print("\nДоступные книги:")
for b in library.available_books():
    print(b.info())

print("\nВыданные книги:")
for b in library.taken_books():
    print(b.info())
