
class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a readable representation of a generic book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize an EBook, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a readable representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize a PrintBook, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a readable representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a Library that uses composition to manage books."""

    def __init__(self):
        """Initialize an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library with their details."""
        for book in self.books:
            print(book)
