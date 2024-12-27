# Data Preprocessing

This document outlines the steps taken to preprocess the data before training the machine learning model.

## Steps Involved:

### 1.1. Data Loading:
- The dataset was loaded from CSV files containing credit card transaction details, including both fraudulent and non-fraudulent transactions.

### 1.2. Handling Missing Values:
- The dataset was inspected for missing values. Since there were no major missing values in the key features, we did not need to perform any imputation or removal of rows.

### 1.3. Handling Imbalanced Data:
- **SMOTE (Synthetic Minority Over-sampling Technique)** was used to address the class imbalance in the dataset. This method synthetically generated samples for the minority class (fraudulent transactions) to balance the dataset.

### 1.4. Feature Engineering:
- The dataset includes several features, including transaction details, time, and user information. We performed encoding and scaling where necessary:
  - **MinMax Scaling** was applied to normalize the data, ensuring that all features had values in the same range to improve model performance.

### 1.5. Data Splitting:
- The dataset was split into training and test sets using an **80/20 split**, ensuring that the model would train on the majority of the data and be evaluated on a separate test set.

## Conclusion:
The preprocessing steps helped prepare the data by handling missing values, normalizing features, and addressing class imbalance. The cleaned data was then ready for model training.
