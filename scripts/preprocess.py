import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)

    X = df.drop(columns=['Class'])
    y = df['Class']

    # Normalize 'Amount' column using Min-Max Scaler
    scaler = MinMaxScaler()
    X[['Amount']] = scaler.fit_transform(X[['Amount']])

    # Handle class imbalance using SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)

    processed_data = pd.concat([pd.DataFrame(X_resampled), pd.DataFrame(y_resampled, columns=['Class'])], axis=1)
    processed_data.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
    
if __name__ == "__main__":
    input_file = 'C:/Code/Credit-Card-Fraud-Detection/data/creditcard.csv' 
    output_file = 'C:/Code/Credit-Card-Fraud-Detection/data/processed_data.csv'  
    preprocess_data(input_file, output_file)
