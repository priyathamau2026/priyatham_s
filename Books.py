from fastapi import APIRouter,HTTPException
from models import Books

router = APIRouter(prefix="/books")

# Dummy data simulating a database
Books_list = {
    1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 10.99},
    2: {"title": "1984", "author": "George Orwell", "price": 12.99},
    3: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 15.99},
    4: {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 11.99},
    5: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 13.99}
}

@router.get("/{Book_id}")
def get_book(Book_id: int):
    book = Books_list.get(Book_id)
    if not book:
        # Return HTTP 404 if not found
        raise HTTPException(status_code=404, detail="Book not found")
    return {"Book_id": Book_id, "details": book}

@router.post("/")
def create_book(book:Books):
    Books_list[len(Books_list) + 1] = book
    # Here you would add code to save the item in a database
    return {"message": " added", "Book": book}