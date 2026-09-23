import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Count books
cursor.execute("SELECT COUNT(*) FROM books")
book_count = cursor.fetchone()[0]

# Count categories
cursor.execute("SELECT COUNT(*) FROM categories")
category_count = cursor.fetchone()[0]

print("Total books:", book_count)
print("Total categories:", category_count)

# Show first 5 books
cursor.execute("""
SELECT
    books.book_id,
    books.title,
    books.price_gbp,
    books.rating,
    books.in_stock,
    books.price_inr,
    categories.category_name
FROM books
JOIN categories
    ON books.category_id = categories.category_id
LIMIT 5
""")

print("\nFirst 5 database records:")

for row in cursor.fetchall():
    print(row)

conn.close()