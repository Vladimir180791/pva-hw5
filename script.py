import csv
import json
from math import ceil

def distribute_books(users, books):
    num_users = len(users)
    num_books = len(books)
    books_per_user = ceil(num_books / num_users)
    
    for i, user in enumerate(users):
        start = i * books_per_user
        end = start + books_per_user
        user["books"] = books[start:end]
        if end >= num_books:
            break 

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