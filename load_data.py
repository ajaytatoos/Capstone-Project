import sqlite3
from scraper import all_books


DB_NAME = "books.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


# Insert categories
categories = sorted(set(book["category"] for book in all_books))

for category in categories:
    cursor.execute(
        """
        INSERT OR IGNORE INTO categories (category_name)
        VALUES (?)
        """,
        (category,)
    )


# Insert books
for book in all_books:

    cursor.execute(
        "SELECT category_id FROM categories WHERE category_name = ?",
        (book["category"],)
    )

    category_id = cursor.fetchone()[0]

    cursor.execute(
        """
        INSERT INTO books
        (title, price_gbp, rating, in_stock, price_inr, category_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            book["title"],
            book["price_gbp"],
            book["rating"],
            book["in_stock"],
            book["price_inr"],
            category_id
        )
    )


conn.commit()
conn.close()

print("Data loaded successfully.")
print("Books loaded:", len(all_books))
print("Categories loaded:", len(categories))