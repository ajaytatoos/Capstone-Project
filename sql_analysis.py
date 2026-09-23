import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()


# SQL Query 1: Count books by category
cursor.execute("""
SELECT
    categories.category_name,
    COUNT(books.book_id) AS total_books
FROM books
JOIN categories
    ON books.category_id = categories.category_id
GROUP BY categories.category_name
ORDER BY total_books DESC
""")

print("Query 1 - Books by category:")

for row in cursor.fetchall():
    print(row)


# SQL Query 2: Average price by category
cursor.execute("""
SELECT
    categories.category_name,
    ROUND(AVG(books.price_gbp), 2) AS average_price_gbp
FROM books
JOIN categories
    ON books.category_id = categories.category_id
GROUP BY categories.category_name
ORDER BY average_price_gbp DESC
""")

print("\nQuery 2 - Average price by category:")

for row in cursor.fetchall():
    print(row)


# SQL Query 3: Top 5 most expensive books
cursor.execute("""
SELECT
    title,
    price_gbp,
    rating,
    categories.category_name
FROM books
JOIN categories
    ON books.category_id = categories.category_id
ORDER BY price_gbp DESC
LIMIT 5
""")

print("\nQuery 3 - Top 5 most expensive books:")

for row in cursor.fetchall():
    print(row)

# SQL Query 4: Average rating by category
cursor.execute("""
SELECT
    categories.category_name,
    ROUND(AVG(books.rating), 2) AS average_rating
FROM books
JOIN categories
    ON books.category_id = categories.category_id
GROUP BY categories.category_name
ORDER BY average_rating DESC
""")

print("\nQuery 4 - Average rating by category:")

for row in cursor.fetchall():
    print(row)

# SQL Query 5: Books currently in stock by category
cursor.execute("""
SELECT
    categories.category_name,
    COUNT(books.book_id) AS in_stock_books
FROM books
JOIN categories
    ON books.category_id = categories.category_id
WHERE books.in_stock = 1
GROUP BY categories.category_name
ORDER BY in_stock_books DESC
""")

print("\nQuery 5 - Books currently in stock by category:")

for row in cursor.fetchall():
    print(row)
    
conn.close() 