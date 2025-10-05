class Book:
    """A class representing a book with title, author, and check-out status."""

    def __init__(self, title, author):
        """Initialize the book with title, author, and check-out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute for availability

    def check_out(self):
        """Check out the book (mark as unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book (mark as available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class to represent a library that manages multiple books."""

    def __init__(self):
        """Initialize the library with an empty book list."""
        self._books = []  # Private list to hold Book objects

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in library.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book titled '{title}' not found in library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
