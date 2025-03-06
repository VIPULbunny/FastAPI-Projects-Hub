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