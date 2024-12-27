# Evaluation Metrics

This document outlines the evaluation metrics used to assess the performance of the Logistic Regression model for credit card fraud detection.

## Metrics Used:

### 1. Test Accuracy:
- **Test Accuracy**: 97.35%  
  The model correctly predicted 97.35% of the total transactions in the test set.

### 2. Classification Report:
The classification report provides the following detailed metrics for both fraudulent and non-fraudulent transactions:

           precision    recall  f1-score   support

       0       0.97      0.98      0.97     56750
       1       0.98      0.97      0.97     56976

accuracy                           0.97    113726

### 3. Precision:
- **Precision for class 0 (non-fraudulent)**: 97%
- **Precision for class 1 (fraudulent)**: 98%
  - Precision measures how many of the predicted positive class transactions were actually positive.

### 4. Recall:
- **Recall for class 0 (non-fraudulent)**: 98%
- **Recall for class 1 (fraudulent)**: 97%
  - Recall measures how many of the actual positive class transactions were correctly predicted.

### 5. F1 Score:
- **F1 Score for class 0 (non-fraudulent)**: 97%
- **F1 Score for class 1 (fraudulent)**: 97%
  - F1 Score provides a balance between precision and recall, offering an overall performance measure.

### 6. Macro Average:
- **Macro Average**: 97%
  - The average of precision, recall, and F1-score across all classes without considering class imbalance.

### 7. Weighted Average:
- **Weighted Average**: 97%
  - The weighted average of precision, recall, and F1-score, accounting for the number of samples in each class.

## Conclusion:
The Logistic Regression model performed well, with high precision and recall for both classes (fraudulent and non-fraudulent transactions). The overall accuracy of the model was 97.35%, making it a robust choice for fraud detection. Future improvements may involve exploring other models like Random Forest or XGBoost.
