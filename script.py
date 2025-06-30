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
        # Определяем сколько книг получит текущий пользователь
        books_count = base_books_per_user + (1 if i < extra_books else 0)
        
        # Добавляем книги пользователю
        users[i]["books"] = books[book_index:book_index + books_count]
        book_index += books_count

def filter_user_data(user):
    """Оставляет только нужные поля пользователя и преобразует книги"""
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
    # Чтение пользователей
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    # Чтение книг
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
    
    # Распределение книг
    distribute_books(users, books)
    
    # Фильтрация данных перед записью
    filtered_users = [filter_user_data(user) for user in users]
    
    # Запись результата
    with open('result.json', 'w') as f:
        json.dump(filtered_users, f, indent=4)

if __name__ == "__main__":
    main()