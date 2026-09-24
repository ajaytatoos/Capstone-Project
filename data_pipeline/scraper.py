import requests
from bs4 import BeautifulSoup


category_urls = {
    "Travel": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "Mystery": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "Historical Fiction": "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
    "Fiction": "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
}


rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


all_books = []


for category, url in category_urls.items():

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    for book in books:

        title = book.h3.a["title"].encode("latin1").decode("utf-8")

        price_text = book.select_one(".price_color").text
        price_gbp = float(
            price_text.replace("Â£", "").replace("£", "").strip()
        )

        rating_text = book.select_one(".star-rating")["class"][1]
        rating = rating_map[rating_text]

        stock_text = book.select_one(".availability").text.strip()
        in_stock = "In stock" in stock_text

        price_inr = round(price_gbp * 105.50, 2)

        all_books.append({
            "title": title,
            "price_gbp": price_gbp,
            "rating": rating,
            "in_stock": in_stock,
            "price_inr": price_inr,
            "category": category
        })


print("Total books scraped:", len(all_books))

print(
    "Categories:",
    sorted(set(book["category"] for book in all_books))
)

print("\nFirst 5 cleaned records:")

for book in all_books[:5]:
    print(book)
    