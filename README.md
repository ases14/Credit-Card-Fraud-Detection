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
The performance of the **Logistic Regression** model is evaluated using the following metrics:

1. **Accuracy**: The proportion of correctly predicted transactions (fraudulent and non-fraudulent).
2. **Precision**: The proportion of correctly predicted fraudulent transactions out of all predicted fraudulent transactions. It answers: "Of all the predicted fraud cases, how many were actually fraud?"
3. **Recall**: The proportion of actual fraudulent transactions that were correctly predicted by the model. It answers: "Of all the actual fraud cases, how many were detected?"
4. **F1 Score**: The harmonic mean of precision and recall. This metric is useful for balancing the trade-off between precision and recall, particularly when dealing with imbalanced datasets.

### Formulae:
- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN)
- **F1 Score** = 2 * (Precision * Recall) / (Precision + Recall)

Where:
- **TP** = True Positives (Fraud predicted as Fraud)
- **FP** = False Positives (Non-fraud predicted as Fraud)
- **FN** = False Negatives (Fraud predicted as Non-fraud)

## Conclusion
The **Logistic Regression** model performs well in detecting fraudulent transactions after handling class imbalance using SMOTE and normalizing the data with MinMaxScaler. The model can accurately classify transactions into fraudulent and non-fraudulent categories, providing valuable insights for fraud detection systems.

### Future Improvements:
- Experiment with more advanced models like **Random Forest**, **XGBoost**, or **Neural Networks** for potentially better performance.
- Consider implementing more sophisticated handling for imbalanced data or exploring different oversampling techniques.
- Investigate methods for **real-time fraud detection** in a production environment.

## How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection
