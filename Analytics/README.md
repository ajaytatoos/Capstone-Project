Module 2 — Analytics Pipeline

Overview
This module implements an end-to-end analytics and machine learning workflow using the Titanic dataset.

The workflow covers exploratory data analysis, data cleaning, statistical analysis, feature preprocessing, classification, model evaluation, class-imbalance handling, hyperparameter tuning, regression analysis, and saving a complete machine learning pipeline.

Project Structure
analytics/
01_eda.ipynb
02_modeling.ipynb
titanic.csv
model_pipeline.joblib
README.md

Dataset

The Titanic dataset is loaded using Seaborn's built-in Titanic dataset.
The raw dataset contains 891 records and 15 columns. The dataset is saved as `titanic.csv` so that subsequent analysis and modelling can use the same committed offline dataset.

Notebook 1 — Exploratory Data Analysis

01_eda.ipynb
This notebook covers:

* Initial dataset inspection and profiling
* Dataset shape, information, and descriptive statistics
* Missing-value analysis
* Data cleaning and missing-value treatment
* Age and fare distribution analysis
* IQR-based outlier detection
* Fare mean, median, and mode
* Survival analysis by sex and passenger class
* Interaction analysis between sex and passenger class
* Correlation analysis using selected numerical variables
* Multiple visualisations describing survival patterns
* Z-score standardisation of age and fare for exploratory analysis

The cleaned dataset is used as the basis for the modelling workflow.

Notebook 2 — Machine Learning Modelling
02_modeling.ipynb

This notebook continues from the cleaned Titanic dataset and covers:

Train/Test Split
* Stratified train/test split
* Target variable: `survived`
* Class-balance verification

Preprocessing
A preprocessing pipeline is used for:
* Median imputation of numerical variables
* Most-frequent imputation of categorical variables
* Standardisation of numerical features
* One-hot encoding of categorical features

The preprocessing is fitted using the training data and then applied to the test data.

Classification Models
Three classification models are trained using the same train/test split:
* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

The Decision Tree is also visualised to inspect its learned structure.

Model Evaluation
The classifiers are evaluated using:
* Confusion matrix
* Accuracy
* Precision
* Recall
* F1 score
* ROC-AUC

Class Imbalance
The effect of class imbalance is examined by comparing:
* Baseline Logistic Regression
* Class-weighted Logistic Regression
* SMOTE-based Logistic Regression

Precision, recall, and F1 score are compared across the approaches.

Random Forest Hyperparameter Tuning
GridSearchCV is used to tune the Random Forest using:
* `n_estimators`
* `max_depth`
* `max_features`

The tuned model is evaluated using cross-validation and out-of-bag (OOB) performance.

Regression Analysis
A multivariate linear regression model is used to predict passenger fare from available passenger characteristics.
Regression performance is evaluated using:
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R²
* Adjusted R²

A residual plot is also used to examine the regression errors and assess the presence of heteroscedasticity.

Saved Model
The final complete machine learning pipeline is saved as:
model_pipeline.joblib
The saved object contains the preprocessing steps and trained estimator so that raw input data can be passed directly to the reloaded pipeline.
The pipeline was reloaded and tested successfully on raw test input.

Reproducibility
To reproduce the analysis:
1. Open `01_eda.ipynb`.
2. Run the exploratory analysis and cleaning workflow.
3. Use the generated `titanic.csv` dataset.
4. Open `02_modeling.ipynb`.
5. Load the committed `titanic.csv`.
6. Run the modelling and evaluation workflow.
7. The completed pipeline is saved as `model_pipeline.joblib`.

Technologies Used
* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib
* Scikit-learn
* imbalanced-learn
* Joblib
* Jupyter/Google Colab
