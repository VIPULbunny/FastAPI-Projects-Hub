# Import FastAPI framework
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional    


# Create a FastAPI app instance
app = FastAPI()

# Define a Book class (not a Pydantic model, just a regular Python class)
class Book:
    # Class-level attribute annotations (not needed but do no harm)
    id: int
    title: str
    author: str
    description: str
    rating: int

    # Constructor to initialize Book objects
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = Field(description = 'ID is not needed on create', default = None)
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1,max_length = 100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "a new book",
                "author": "codingwithvipul",
                "description": "A new Description of a book",
                "rating": 5
            }
        }
    }


# Create a list of Book objects (acting as a mock database)
BOOKS = [
    Book(1, 'Computer science Pro', 'codingwithroby', 'A very nice Book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great Book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome Book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1),
]

# Endpoint to return all books
@app.get("/books")
async def read_all_books():
    # Convert each Book object to dictionary before returning
    return [book.to_dict() for book in BOOKS]

# Endpoint to return a specific book by ID (e.g., /books/1)
@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book.to_dict()
    # If no book found, raise a 404 error
    raise HTTPException(status_code=404, detail="Item Not Found")

# Endpoint to filter books by rating using query parameter (e.g., /books/?book_rating=5)
@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    filtered_books = [book.to_dict() for book in BOOKS if book.rating == book_rating]
    return filtered_books

# Endpoint to filter books by published year using query parameter (e.g., /books/publish/?published_date=2029)
@app.get("/books/publish/")
async def read_book_by_published_date(published_date: int = Query(gt=1999, lt=2031)):
    filtered_books = [book.to_dict() for book in BOOKS if book.published_date == published_date]
    return filtered_books
