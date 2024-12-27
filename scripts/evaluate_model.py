import pickle
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def evaluate_model(model_file, test_file):
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    test_data = pd.read_csv(test_file)
    X_test = test_data.drop(columns=['Class'])
    y_test = test_data['Class']

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Test Accuracy (Logistic Regression):", accuracy)
    print("Classification Report (Logistic Regression):\n", classification_report(y_test, y_pred))

    # Confusion Matrix visualization
    conf_matrix = confusion_matrix(y_test, y_pred)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.show()

if __name__ == "__main__":
    model_file = 'C:/Code/Credit-Card-Fraud-Detection/models/model.pkl'
    test_file = 'C:/Code/Credit-Card-Fraud-Detection/data/processed_data.csv' 
    evaluate_model(model_file, test_file)
