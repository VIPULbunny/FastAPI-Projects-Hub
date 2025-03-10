from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
# @app.get("/")
# async def root():
#     return {"message": "Welcome to my FastAPI app!"}

@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello Vipul"}

@app.get("/books")
async def read_all_books():
    return BOOKS

# Get book by title
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}

# Get books by category using query parameter
@app.get("/books/category/")
async def read_category_by_query(category: str):
    books_to_return = [book for book in BOOKS if book.get('category').casefold() == category.casefold()]
    return books_to_return if books_to_return else {"message": "No books found in this category"}

# Get books by author and category using query parameters
@app.get("/books/author/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = [book for book in BOOKS if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold()]
    return books_to_return if books_to_return else {"message": "No books found for this author in this category"}

# Create a new book
@app.post("/books/create_book")
async def create_book(new_book: dict = Body(...)):
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

#UPdate the existing books
@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


#Delete the Book
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
