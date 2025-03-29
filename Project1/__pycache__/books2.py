# Import FastAPI and necessary modules
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field  # For data validation and request body structure
from typing import Optional  # To allow optional fields
from starlette import status  # For HTTP status codes

# Create a FastAPI app instance
app = FastAPI()

# Define a Book class (not a Pydantic model, just a regular Python class)
class Book:
    # Class-level attribute annotations (not required, but add clarity)
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    # Constructor to initialize Book objects
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# Define a Pydantic model for request body validation when creating/updating books
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)  # Title must be at least 3 characters
    author: str = Field(min_length=1)  # Author name must not be empty
    description: str = Field(min_length=1, max_length=100)  # Description must be 1-100 chars
    rating: int = Field(gt=0, lt=6)  # Rating should be between 1 and 5
    published_date: int = Field(gt=1999, lt=2031)  # Valid year range: 2000-2030

    # Example schema to show in API docs (Swagger UI)
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "a new book",
                "author": "codingwithvipul",
                "description": "A new Description of a book",
                "rating": 5,
                "published_date": 2029
            }
        }
    }

# Create a list of Book objects (acts as an in-memory mock database)
BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice Book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great Book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome Book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]

# API endpoint to get all books
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    # FastAPI can't directly return non-serializable objects (like Book)
    # In real implementation, you'd convert to dict or use a Pydantic model
    return BOOKS  # Here returning as-is for simplicity

# API endpoint to get a specific book by its ID
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):  # Validate that ID is greater than 0
    for book in BOOKS:
        if book.id == book_id:
            return book
    # If book not found, raise 404 error
    raise HTTPException(status_code=404, detail='Item Not Found')

# API endpoint to filter books by rating
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):  # Validate rating between 1 and 5
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return
