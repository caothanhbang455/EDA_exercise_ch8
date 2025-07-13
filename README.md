# Logistic regression with feature engineering and text preprocessing

This repo is designed for practicing feature engineering, scaling, text processing, and building a machine learning pipeline using logistic regression from the `scikit-learn` library.

## Objective

The objective is to demonstrate how to:
- Apply preprocessing techniques for numerical and textual data
- Use scalers such as `StandardScaler` or `MinMaxScaler`
- Build modular and reusable pipelines
- Train and evaluate a logistic regression classifier effectively

## Dataset

- **Location:** [Google Drive dataset link](https://drive.google.com/file/d/1KPEF3iEjbEfhzp67Lj2tQy7aD7O4rEii/view?usp=sharing)  
- **Format:** CSV file  
- **Includes:**
  - Structured numerical features
  - One or more columns containing textual data

## Key steps

1. **Import libraries**  
   Load essential packages for data manipulation, visualization, and modeling.

2. **Load dataset**  
   Read the dataset from the provided source and perform initial exploration.

3. **Exploratory data analysis (EDA)**  
   Understand distributions, detect missing values, and analyze text features.

4. **Preprocessing**
   - Handle missing values
   - Apply scaling to numerical features
   - Tokenize and clean text data
   - Use `TfidfVectorizer` or `CountVectorizer` for feature extraction from text

5. **Feature engineering**
   - Create or transform new features if needed
   - Concatenate numerical and text features for modeling

6. **Build machine learning pipeline**
   - Combine preprocessing steps using `ColumnTransformer` and `Pipeline`
   - Fit a logistic regression model

7. **Model evaluation**
   - Use accuracy, precision, recall, and F1-score
   - Optionally visualize confusion matrix and ROC curve

## Technologies used

- Python 3.x
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- nltk / spaCy (if text cleaning is required)

## How to run

1. Clone the repository or download the notebook.
2. Install required dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
