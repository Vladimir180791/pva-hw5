import csv
import json
from math import floor

def distribute_books(users, books):
    num_users = len(users)
    num_books = len(books)
    base_books_per_user = num_books // num_users
    extra_books = num_books % num_users
    
    book_index = 0
    for i in range(num_users):
        books_count = base_books_per_user + (1 if i < extra_books else 0)
        
        users[i]["books"] = books[book_index:book_index + books_count]
        book_index += books_count

def filter_user_data(user):
    return {
        "name": user.get("name"),
        "gender": user.get("gender"),
        "address": user.get("address"),
        "age": user.get("age"),
        "books": [
            {
                "title": book.get("title"),
                "author": book.get("author"),
                "pages": book.get("pages"),
                "genre": book.get("genre")
            }
            for book in user.get("books", [])
        ]
    }
def main():
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    books = []
    with open('books.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append({
                "title": row["Title"],
                "author": row["Author"],
                "pages": int(row["Pages"]),
                "genre": row["Genre"]
            })
    
    distribute_books(users, books)
    
    with open('result.json', 'w') as f:
        json.dump(users, f, indent=4)

if __name__ == "__main__":
    main()