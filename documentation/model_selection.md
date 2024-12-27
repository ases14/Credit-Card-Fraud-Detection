# Model Selection

This document explains the process followed to select the best machine learning model for the fraud detection task.

## Model Chosen:
- **Logistic Regression** was chosen as the base model for this task. Logistic Regression is a commonly used algorithm for binary classification problems like fraud detection, where the goal is to predict if a transaction is fraudulent or not.

## Reasons for Choosing Logistic Regression:
- **Interpretability**: Logistic Regression provides insights into the impact of individual features on the prediction, which is helpful in understanding fraud detection patterns.
- **Efficiency**: Logistic Regression is computationally efficient and works well with balanced datasets after handling class imbalance using SMOTE.
- **Performance**: After applying necessary preprocessing, Logistic Regression showed strong performance in the evaluation metrics.

## Model Evaluation:
- We evaluated the model based on precision, recall, F1 score, and accuracy. The Logistic Regression model performed well across these metrics, demonstrating its suitability for the task.

## Future Models to Consider:
- **Random Forest**: Could be explored for better handling of complex patterns and feature interactions.
- **XGBoost**: Known for its ability to work well with imbalanced datasets and achieving high performance in classification tasks.

