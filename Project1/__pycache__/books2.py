# Import FastAPI framework
from fastapi import FastAPI
from pydantic import BaseModel


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
    id: int
    title: str
    author: str
    description: str
    rating: int

# Create a list of Book objects (acting as a mock database)
BOOKS = [
    Book(1, 'Computer science Pro', 'codingwithroby', 'A very nice Book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great Book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome Book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1),
]

# API endpoint to return all books
@app.get("/books")
async def read_all_books():
    # FastAPI cannot directly return custom Python objects (Book instances)
    # Need to convert each Book object to a dictionary
    return BOOKS  # Convert objects to dict before returning

@app.post("/create-book")
async def create_book(book_request : BookRequest):
    # print(type(book_request))
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOKS.append(new_book)

