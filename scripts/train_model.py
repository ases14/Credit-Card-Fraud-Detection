import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


def train_and_evaluate_model(input_file,model_file):
    data = pd.read_csv(input_file)
    
    # Feature-target split
    X = data.drop(columns=['Class'])
    y = data['Class']
    
    # Train-test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train Logistic Regression model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"done")

    try:
        with open(model_file, 'wb') as f:
            pickle.dump(model, f)
        print(f"Model saved as {model_file}")
    except Exception as e:
        print(f"Error saving the model: {e}")
    
    print(f"done")

    accuracy = accuracy_score(y_test, y_pred)
    print("Test Accuracy (Logistic Regression):", accuracy)
    print("Classification Report (Logistic Regression):\n", classification_report(y_test, y_pred))

    conf_matrix = confusion_matrix(y_test, y_pred)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.show()


if __name__ == "__main__":
    input_file = 'C:/Code/Credit-Card-Fraud-Detection/data/processed_data.csv'
    model_file = 'C:/Code/Credit-Card-Fraud-Detection/models/model.pkl'
    train_and_evaluate_model(input_file, model_file)
