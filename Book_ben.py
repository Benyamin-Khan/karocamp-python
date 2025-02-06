class BOOK:
    def __init__(self, title: str, author: str, isbn: int, is_borrowed: bool = False):
        self.title: str = title
        self.author: str = author
        self.isbn: int = isbn
        self.is_borrowed: bool = is_borrowed

    def borrow_book(self):
        if self.is_borrowed:
            raise ValueError(f"The book '{self.title}' has already been borrowed.")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError(f"The book '{self.title}' has not been borrowed.")
        self.is_borrowed = False


class Member:
    def __init__(self, name: str, member_id: str, borrowed_books: bool):
        self.name: str = name
        self.member_id: str = member_id
        self.borrowed_books: list = []

    def borrow(self, book):
        if book.is_borrowed:
            raise ValueError(
                f"The book '{book.title}' cannot be borrowed because it has already been borrowed."
            )

        self.borrowed_books.append(book)
        book.borrow_book()

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise ValueError(f"The book '{book.title}' has not been borrowed by you.")
        self.borrowed_books.remove(book)
        book.return_book()


class Library:
    def __init__(self, books: list = None, members: list = None):
        self.books: list = []
        self.members: list = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, isbn, member_id):
        book = self._find_book_by_isbn(isbn)
        member = self._find_member_by_id(member_id)

        if book is None:
            raise ValueError("The requested book was not found.")
        if member is None:
            raise ValueError("The member is not registered in the system.")

        member.borrow(book)

    def return_book(self, isbn, member_id):
        book = self._find_book_by_isbn(isbn)
        member = self._find_member_by_id(member_id)

        if book is None:
            raise ValueError("کتاب مورد نظر پیدا نشد.")
        if member is None:
            raise ValueError("عضو مورد نظر در سیستم ثبت نشده است.")

        member.return_book(book)

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        if not available_books:
            print("There are no available books at the moment.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author} - ISBN: {book.isbn}")

    def _find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def _find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
