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
    id: Optional[int] = None
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1,max_length = 100)
    rating: int = Field(gt=0, lt=6)

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
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book : Book):

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book
