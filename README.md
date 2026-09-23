Module 1 – Books Web Scraping and Data Analysis
Project Overview
This project demonstrates a complete data pipeline for collecting, cleaning, storing, and analysing book data from the Books to Scrape website.

The project includes:
* Web scraping using Python
* Data cleaning and transformation
* SQLite database design
* SQL analysis
* Pandas analysis
* Data merging using Pandas
* Reproducible project dependencies

Dataset
The project uses book information collected from Books to Scrape.

The scraper collected:
71 books
4 categories

Travel
Mystery
Historical Fiction
Fiction

Data fields

The final dataset contains:
title` – Book title
price_gbp` – Book price in GBP
rating` – Rating from 1 to 5
in_stock` – Whether the book is currently in stock
price_inr` – Converted price in INR
category` – Book category

The INR conversion used in the project is:

"price_inr = price_gbp × 105.50"

Project Structure

Module - 1 Final

1.scraper.py
2.database.py
3.load_data.py
4.verify_database.py
5.sql_analysis.py
6.analysis.ipynb
7.books.db
8.requirements.txt
9.README.md

1. Web Scraping

The "scraper.py" file collects book information from four book categories.

The scraper uses:
requests
BeautifulSoup

The scraped data is cleaned and converted into the required fields before being stored in a Python list.

The scraper successfully collected **71 books** across **4 categories**.

2. SQLite Database

The "database.py" file creates the SQLite database and the required tables.

Categories table

The "categories" table contains:

category_id` – Primary key
category_name` – Category name

Books table

The "books" table contains:

* `book_id` – Primary key
* `title`
* `price_gbp`
* `rating`
* `in_stock`
* `price_inr`
* `category_id` – Foreign key

The "category_id" field connects the "books" table to the "categories" table.

3. Loading Data

The "load_data.py" file loads the scraped book data into the SQLite database.

The final database contains:
71 books
4 categories

4. SQL Analysis

The "sql_analysis.py" file contains five SQL analysis queries.

Query 1 – Books by category
Counts the number of books available in each category.

Query 2 – Average price by category
Calculates the average GBP price for each category.

Query 3 – Top 5 most expensive books
Returns the five books with the highest GBP prices.

Query 4 – Average rating by category
Calculates the average book rating for each category.

Query 5 – Books currently in stock by category
Counts the books currently marked as in stock for each category.

5. Pandas Analysis
The "analysis.ipynb" notebook performs equivalent analysis using Pandas.

The notebook demonstrates:

* Loading SQLite data using "pd.read_sql()"
* Books by category
* Average price by category
* Top 5 most expensive books
* Average rating by category
* Books currently in stock by category
* Combining database tables using Pandas "merge()"

The Pandas results were checked against the SQL results.

6. How to Run the Project

Create and activate the virtual environment

On Windows PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1


Install dependencies
pip install -r requirements.txt


Run the scraper
python scraper.py


Create the database
python database.py


Load the scraped data
python load_data.py


Verify the database
python verify_database.py


Run SQL analysis
python sql_analysis.py

Run Pandas analysis
Open:
analysis.ipynb


Select the project's ".venv" Python environment and run the notebook cells.

Project Outcome
The completed project demonstrates a simple end-to-end data workflow:

Web Scraping
     ↓
Data Cleaning
     ↓
SQLite Database
     ↓
SQL Analysis
     ↓
Pandas Analysis
     ↓
Results

The project successfully processes "71 books across 4 categories" and provides both SQL and Pandas-based analysis of the collected data.
