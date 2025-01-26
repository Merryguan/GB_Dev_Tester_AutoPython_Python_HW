"""
 Семинар 14. Основы тестирования.

 Задание №2. Тестирование класса с использованием unittest.

 Условие:
 Напишите класс Library,
 который управляет книгами.
 Класс должен поддерживать
 следующие методы:
 - add_book(title): добавляет книгу в библиотеку.
 - remove_book(title): удаляет книгу из библиотеки.
 - list_books(): возвращает список всех книг в библиотеке.
 При попытке удалить книгу,
 которая не существует,
 должно выбрасываться исключение BookNotFoundError.
 Для тестирования используйте unitest.
"""

# Решение:
import unittest


class BookNotFoundError(Exception):
    def __init__(self):
        super().__init__("Книга не найдена в библиотеке.")


class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, title):
        self.books.add(title)

    def remove_book(self, title):
        if title not in self.books:
            raise BookNotFoundError()
        self.books.remove(title)

    def list_books(self):
        return list(self.books)


class TestLibraryCase(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_1(self):
        self.library.add_book("Война и мир")
        self.assertIn("Война и мир", self.library.list_books())

    def test_2(self):
        self.library.add_book("Война и мир")
        self.library.remove_book("Война и мир")
        self.assertNotIn("Война и мир", self.library.list_books())

    def test_3(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")


if __name__ == "__main__":
    unittest.main(verbosity=2)