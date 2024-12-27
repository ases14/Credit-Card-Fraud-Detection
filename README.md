# Credit Card Fraud Detection

## Overview
This project focuses on detecting fraudulent credit card transactions using **Logistic Regression**. The goal is to predict whether a given transaction is fraudulent or not based on transaction details such as amount, time, and other relevant features.

## Approach
The project follows a structured approach to fraud detection:
1. **Data Preprocessing**: Cleaning and preparing the data to make it ready for training the model.
2. **Model Training**: Training a **Logistic Regression** model to classify transactions as fraudulent or non-fraudulent.
3. **Model Evaluation**: Evaluating the model's performance using metrics like accuracy, precision, recall, and F1 score.

## Data Preprocessing
The following steps were followed to preprocess the data:

1. **Handling Missing Values**: 
   - Missing values were handled appropriately. For numerical features, the missing values were imputed using the mean or median (depending on the distribution of the feature). For categorical features, the most frequent value was used for imputation.

2. **Feature Engineering**: 
   - The dataset contains both numerical and categorical features. These features were processed to be suitable for machine learning models.

3. **Class Imbalance Handling**:
   - The dataset has an imbalanced distribution of fraudulent and non-fraudulent transactions. To handle this, **SMOTE (Synthetic Minority Over-sampling Technique)** was used to oversample the minority class (fraudulent transactions) and create synthetic data points, balancing the dataset.

4. **Data Normalization**:
   - **MinMaxScaler** was used to normalize the features, scaling all the data to a range between 0 and 1. This ensures that all features contribute equally to the model and that the model isn't biased by features with larger ranges.

5. **Outlier Handling**:
   - Outliers were not explicitly handled in this project, as the focus was primarily on preprocessing for class imbalance and normalization.

## Model Selection
The primary model used in this project is **Logistic Regression**, which is a simple yet effective model for binary classification tasks. Logistic Regression is chosen for its ability to handle probabilistic outcomes, making it suitable for fraud detection where the goal is to predict the likelihood of fraud.

- **Logistic Regression** is used to predict whether a transaction is fraudulent or not (binary classification).
- The model was trained using the **processed dataset** after handling class imbalance and normalizing the features.

## Evaluation Metrics

The **Logistic Regression** model was evaluated on various metrics to understand its performance in detecting fraudulent transactions.

### Test Accuracy:
- **Test Accuracy**: 97.35%  
  The model correctly predicted 97.35% of the total transactions in the test set, demonstrating a high level of accuracy.

### Classification Report:
The classification report provides detailed metrics for both classes (fraudulent and non-fraudulent transactions):


#### Metrics Explanation:
- **Precision**: 
  - Precision for class 0 (non-fraudulent): **97%**
  - Precision for class 1 (fraudulent): **98%**
  - Precision indicates the proportion of correctly predicted fraudulent transactions (class 1) out of all transactions predicted as fraudulent.
  
- **Recall**: 
  - Recall for class 0 (non-fraudulent): **98%**
  - Recall for class 1 (fraudulent): **97%**
  - Recall indicates the proportion of actual fraudulent transactions (class 1) that were correctly identified by the model.
  
- **F1 Score**: 
  - F1 Score for class 0 (non-fraudulent): **97%**
  - F1 Score for class 1 (fraudulent): **97%**
  - F1 score is the harmonic mean of precision and recall, offering a balance between them.
  
- **Accuracy**: 97.35%
  - The overall accuracy of the model is very high, with the model correctly classifying both fraudulent and non-fraudulent transactions.

- **Macro Average**: 97%
  - The average of precision, recall, and F1-score across all classes, without considering class imbalance.

- **Weighted Average**: 97%
  - The weighted average of precision, recall, and F1-score, accounting for the number of samples in each class.

### Conclusion:
The **Logistic Regression** model demonstrates robust performance in detecting fraudulent transactions with high precision, recall, and F1 scores. The model performs well across both classes, maintaining a balanced prediction between fraudulent and non-fraudulent transactions. The results indicate that the model is capable of effectively identifying fraudulent transactions while minimizing false positives and false negatives.

### Future Work:
- Further tuning of the model hyperparameters could improve performance.
- Experimenting with other models like **Random Forest** or **XGBoost** may yield better results, especially in dealing with imbalanced datasets.


## How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection
