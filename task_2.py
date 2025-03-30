from abc import ABC, abstractmethod
import logging
from typing import List

logging.basicConfig(level=logging.INFO)

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> None:
        if not self.books:
            print(f'Library is empty.')
        else:
            for book in self.books:
                print(book)


class LibraryStorage:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f'Book with name "{title}" was added successfully')

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        print(f'Book with name "{title}" was removed successfully')

    def show_books(self) -> None:
        self.library.show_books()


def main() -> None:
    library = Library()
    storage = LibraryStorage(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = int(input("Enter book year: ").strip())
            storage.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            storage.remove_book(title)
        elif command == "show":
            storage.show_books()
        elif command == "exit":
            break
        else:
            print(f'Invalid command. Please try again.')


if __name__ == "__main__":
    main()
