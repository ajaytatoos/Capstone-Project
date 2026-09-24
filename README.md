Zepto AI/ML Capstone Project
This repository contains the complete Zepto AI/ML capstone project with three modules covering data engineering, analytics and machine learning, and an AI-powered support assistant.

Repository Structure

Capstone-Project/
├── data_pipeline/
├── analytics/
├── support_assistant/
└── README.md

Module 1 — Data Pipeline
The data pipeline module scrapes book data using Requests and BeautifulSoup, cleans and transforms the data, stores it in a normalized SQLite database, and performs SQL and Pandas analysis.

Design Decisions
* Requests and BeautifulSoup are used for web scraping.
* SQLite is used for lightweight relational storage.
* Separate category and book tables provide normalized database design.
* SQL and Pandas are used for analysis and validation.

Run
cd data_pipeline
pip install -r requirements.txt
python scraper.py
python database.py
python load_data.py
python verify_database.py
python sql_analysis.py

The analysis notebook can then be opened and executed.

Module 2 — Analytics and Machine Learning
The analytics module uses the Titanic dataset for exploratory data analysis, preprocessing, classification, model comparison, hyperparameter tuning, and regression analysis.
Design Decisions
* The Titanic dataset is loaded once and saved as `titanic.csv` for reproducibility.
* Missing values and outliers are handled during the EDA and cleaning process.
* A preprocessing pipeline is used to prevent data leakage.
* Multiple classification models are compared using accuracy, F1-score, and ROC-AUC.
* Random Forest hyperparameters are tuned using GridSearchCV.
* A regression task is included to evaluate fare prediction.

Run
Open and run the notebooks in:
analytics/01_eda.ipynb
analytics/02_modeling.ipynb

Module 3 — Support Assistant
The support assistant is a policy-based RAG application for answering Zepto support questions. It uses document embeddings, ChromaDB retrieval, LangGraph workflow orchestration, structured prompting, Pydantic validation, and a FastAPI API.
Design Decisions
* Sentence Transformers are used to create document embeddings.
* ChromaDB is used for vector storage and similarity search.
* LangGraph manages the classification, retrieval/answer, and direct-answer workflow.
* Structured prompting helps keep responses focused on Zepto policies.
* Pydantic provides structured API output validation.
* FastAPI exposes the `/ask` endpoint.
* An offline mock mode is included for deterministic testing.

Run
cd support_assistant
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000

The API endpoint is:
POST /ask

End-to-End Project Flow
Module 1
Web Scraping → Data Cleaning → SQLite → SQL/Pandas Analysis
Module 2
Titanic Data → EDA → Cleaning → Preprocessing → ML Models → Evaluation
Module 3
Policy Documents → Embeddings → ChromaDB → Retrieval → LangGraph → FastAPI


Technologies
* Python
* Pandas
* NumPy
* BeautifulSoup
* SQLite
* Seaborn
* Matplotlib
* Scikit-learn
* Imbalanced-learn
* Joblib
* Sentence Transformers
* ChromaDB
* LangGraph
* Pydantic
* FastAPI
* Docker

Project Objective
The project demonstrates an end-to-end AI/ML workflow covering data collection, data engineering, analytics, machine learning, and retrieval-augmented AI application development.
