# Create a class Book
class Book:
    total_books = 0  # Class variable to keep track of total books

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increases the class variable

# Add a new book
Book.increment_book_count()

# Add another new book
Book.increment_book_count()

# Print the total number of books
print("Total books:", Book.total_books)
