class Book:
    """A class representing a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False


    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_checked_out(self):
        return self.__is_checked_out
    
        

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"Book added: {book}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_checked_out():
                book.check_out()
                print(f"Book checked out: {book}")
                return
        print("Book not available or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_checked_out():
                book.return_book()
                print(f"Book returned: {book}")
                return
        print("Book not found or was not checked out.")

    def list_available_books(self):
        print("\nAvailable books:")
        available = [book for book in self.books if not book.is_checked_out()]
        if available:
            for book in available:
                print(book)
        else:
            print("No books available.")
