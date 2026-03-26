class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print("This book is available and has been checked out.")
        elif not self.available: print('This book is already checked out.')

    def return_book(self):
        if self.available: print("Book is still here.")
        elif not self.available:
            self.available = True
            print("Book has been returned.")

python_book = Book("Python for Everybody", "The Khai")
finance_book = Book("Rich Dad Poor Dad", "Robert Kiyosaki")

python_book.checkout()
print(f"{python_book.title} status: {python_book.available}")
python_book.checkout()
print(f"{python_book.title} status: {python_book.available}")

print(f"{finance_book.title} status: {finance_book.available}")


