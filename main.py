from fastapi import FastAPI, HTTPException
from database import db
from models.book import Book
from bson import ObjectId
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "مرحباً بك في FastAPI"}

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    new_book = await db.books.insert_one(book.dict())
    created_book = await db.books.find_one({"_id": new_book.inserted_id})   
    # the name of the table it is there books you can change it by any name you want it 
    return created_book

@app.get("/books/", response_model=List[Book])
async def get_books():
    books = await db.hello.find().to_list(100)
    return books